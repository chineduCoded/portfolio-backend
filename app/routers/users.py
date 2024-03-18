from datetime import datetime, timezone
from typing import Annotated, List
from fastapi import APIRouter, status, HTTPException, Depends
from app.models.user import UserInCreate, UserCreateResponse, UserInDB, User, CountUser
from app.database.db import user_collection
from app.utils.hashing import get_hashed_password
from pymongo import ASCENDING
from bson import ObjectId
from app.utils.security import get_current_user

router = APIRouter()


@router.post("/", response_model=UserCreateResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserInCreate):
    """Register a new user."""
    await user_collection.create_index([("username", ASCENDING), ("email", ASCENDING)])

    existing_user = await user_collection.find_one({
        "$or": [
            {"username": user.username},
            {"email": user.email}
        ]
    })

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User account already exists."
        )

    db_user = UserInDB(**user.model_dump())
    db_user.password = get_hashed_password(user.password)
    db_user.created_at = datetime.now(timezone.utc)
    
    new_user = await user_collection.insert_one(db_user.model_dump())
    
    return UserCreateResponse(
        message="User created successfully",
        id=new_user.inserted_id
    )

@router.get("/count", response_model=CountUser, status_code=status.HTTP_200_OK)
async def count_users():
    """Count the total number of users"""
    total_users = await user_collection.count_documents({})

    return CountUser(total_users=total_users)


@router.get("/", response_model=List[User], status_code=status.HTTP_200_OK)
async def get_users(length: int = 10):
    """Get all users"""
    users = await user_collection.find().to_list(length=length)

    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No users found in the database."
        )
    
    return [User(**user) for user in users]


@router.get("/{id}", response_model=User, status_code=status.HTTP_200_OK)
async def get_user(id: str, current_user: User = Depends(get_current_user)) -> User:
    """Get a user"""
    user = await user_collection.find_one({"_id": ObjectId(id)})

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist."
        )

    if user["username"] != current_user.username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to access other user's information."
        )
    
    return User(**user)




@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: str, current_user: User = Depends(get_current_user)):
    """Delete a user"""
    user = await user_collection.find_one({"_id": ObjectId(id)})

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist."
        )
        
    if user["username"] != current_user.username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to delete other user's information."
        )

    await user_collection.delete_one({"_id": ObjectId(id)})

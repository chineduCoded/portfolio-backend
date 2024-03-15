from datetime import datetime, timezone
from fastapi import APIRouter, status, HTTPException
from app.models.user import UserInCreate, UserInResponse, User
from app.database.db import user_collection
from app.utils.hashing import get_hashed_password
from pymongo import ASCENDING
from bson import ObjectId

router = APIRouter()


@router.post("/", response_model=UserInResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserInCreate):
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
    
    hashed_password = get_hashed_password(user.password)
    new_user = await user_collection.insert_one({
        "username": user.username,
        "email": user.email,
        "password": hashed_password,
        "created_at": datetime.now(timezone.utc)
    })
    


    return UserInResponse(
        message="User created successfully",
        id=new_user.inserted_id
    )

@router.get("/{id}", response_model=User)
async def get_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})

    try:
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {id} does not exists."
            )
        # user["_id"] = str(user["_id"])

        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Something went wrong: {e}"
        )


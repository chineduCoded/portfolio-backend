from datetime import datetime, timezone
from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException
from app.database.db import skill_collection
from app.models.skill import SkillInCreate, SkillResponse, SkillInDB, Skill
from app.models.user import User
from app.utils.security import get_current_user
from bson import ObjectId

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SkillResponse)
async def create_skill(skill_data: SkillInCreate, current_user: Annotated[User, Depends(get_current_user)]):
    db_skill = SkillInDB(**skill_data.model_dump())
    db_skill.created_at = datetime.now(timezone.utc)
    db_skill.owner = current_user.username

    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authorized."
        )

    new_skill = await skill_collection.insert_one(db_skill.model_dump())

    return SkillResponse(
        message="Skill created successfully",
        id=new_skill.inserted_id
    )

@router.get("/{id}", response_model=Skill, status_code=status.HTTP_200_OK)
async def get_skill(id: str, current_user: Annotated[User, Depends(get_current_user)]):
    skill = await skill_collection.find_one({"_id": ObjectId(id)})

    if not skill:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User does not exists."
            )
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="unauthorized."
        )
    
    return Skill(**skill)
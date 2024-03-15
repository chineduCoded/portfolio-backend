from typing import Optional
from fastapi import HTTPException, status
from pydantic import EmailStr
from app.crud.user import get_user, get_user_by_email

async def check_username_and_email(
        db,
        username: Optional[str] = None,
        email: Optional[EmailStr] = None,
):
    if username:
        user_by_username = await get_user(db, username)
        if user_by_username:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Username already exists. Please use another username.",
            )
    if email:
        user_by_email = await get_user_by_email(db, email)
        if user_by_email:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Email already exists. Please use another email.",
            )
    
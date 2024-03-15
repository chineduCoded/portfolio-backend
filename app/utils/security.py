# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from typing import Union, Annotated
# from datetime import datetime, timedelta, timezone
# from jose import jwt, JWTError
# from app.config import settings
# from app.models.user import OauthTokenData
# from app.utils.hashing import verify_password
# from app.crud.user import get_user
# from app.database.db import users




# oauth2_scheme = OAuth2PasswordBearer(tokenUrl=settings.token_url)

# ACCESS_TOKEN_EXPIRE_MINUTES = 10
# REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
# ALGORITHM = "HS256"
    
# async def authenticate_user(username: str, password: str):
#     user = await get_user(users, username)

#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user

# def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.now(timezone.utc) + expires_delta
#     else:
#         expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, settings.jwt_secret_key, algorithm=ALGORITHM)

#     return encoded_jwt

# def create_refresh_token(data: dict, expires_delta: Union[timedelta, None] = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.now(timezone.utc) + expires_delta
#     else:
#         expire = datetime.now(timezone.utc) + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, settings.jwt_refresh_secret_key, algorithm=ALGORITHM)

#     return encoded_jwt



# async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )

#     try:
#         payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")

#         if username is None:
#             raise credentials_exception
#         token_data = OauthTokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#     user = await get_user(users, username=token_data.username)

#     if user is None:
#         raise credentials_exception
#     return user

# async def get_current_active_user(
#         current_user: Annotated[User, Depends(get_current_user)]
# ):
#     if current_user.is_active == False:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Inactive user"
#         )
# from typing import Annotated
# from datetime import timedelta
# from fastapi import APIRouter, HTTPException, Query, status, Depends, Body
# from fastapi.security import OAuth2PasswordRequestForm


# from app.utils.security import authenticate_user, create_access_token

# from app.models.user import OauthToken

# router = APIRouter()


# @router.post("/login", response_model=OauthToken)
# async def login_for_access_token(
#     form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
# ) -> OauthToken:
#     user = authenticate_user(form_data.username, form_data.password)

#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"}
#         )
#     access_token_expires = timedelta(minutes=10)
#     access_token = create_access_token(
#         data={"sub": user.username},
#         expires_delta=access_token_expires
#     )

#     return OauthToken(
#         access_token=access_token,
#         token_type="bearer"
#     )
    


    
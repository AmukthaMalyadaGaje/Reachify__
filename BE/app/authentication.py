# app/authentication.py
from fastapi import APIRouter, Depends, HTTPException, status
from app.models import Token, UserCreate, UserLogin
from app.crud import create_user, get_user_by_username
from app.services import create_access_token, verify_user_password
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/signup", response_model=Token)
async def signup(user_create: UserCreate):
    user = await create_user(user_create)
    if user:
        token = create_access_token(data={"sub": user.username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="User already exists")


@router.post("/login", response_model=Token)
async def login(user_login: UserLogin):
    user = await get_user_by_username(user_login.username)
    if not user or not await verify_user_password(user, user_login.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return payload

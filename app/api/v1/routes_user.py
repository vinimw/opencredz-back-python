from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from ...schemas import user as user_schema, token as token_schema
from ...services import user_service
from ...core import security
from ..deps import get_db, get_current_user

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

@router.post("/register", response_model=user_schema.UserOut)
def register(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    if user_service.get_user_by_username(db, user.username):
        raise HTTPException(status_code=400, detail="Usuário já existe")
    return user_service.create_user(db, user)

@router.post("/login", response_model=token_schema.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = user_service.get_user_by_username(db, form_data.username)
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = security.create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=user_schema.UserOut)
def read_users_me(current_user = Depends(get_current_user)):
    return current_user

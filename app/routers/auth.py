from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.auth import LoginSchema, TokenResponse
from app.models.user import User
from app.auth import jwt
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/login", response_model=TokenResponse)
def login(user_cred: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_cred.email).first()
    if not user or not pwd_context.verify(user_cred.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = jwt.create_access_token({"sub": user.email})
    return {"access_token": access_token}

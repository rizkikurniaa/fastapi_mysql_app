from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from app.auth import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")  # URL login endpoint

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = jwt.verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import user as user_schema
from app.database import SessionLocal
from app.crud import user as user_crud
from fastapi import HTTPException

router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[user_schema.UserResponse])
def read_users(db: Session = Depends(get_db)):
    return user_crud.get_users(db)

@router.post("/", response_model=user_schema.UserResponse)
def create_new_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db, user)

@router.get("/{user_id}", response_model=user_schema.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=user_schema.UserResponse)
def update_user(user_id: int, updated_user: user_schema.UserCreate, db: Session = Depends(get_db)):
    user = user_crud.update_user(db, user_id, updated_user)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted = user_crud.delete_user(db, user_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}

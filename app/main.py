from fastapi import FastAPI
from app.database import engine, Base         # ✅ Import Base dari database.py (baik!)
from app.models import user                   # ✅ Wajib untuk memastikan model User terbaca
from app.routers import user as user_router   # ✅ Untuk include endpoint dari routers/user.py
from app.routers import auth as auth_router

Base.metadata.create_all(bind=engine)         # ✅ Membuat tabel-tabel di database

app = FastAPI()
app.include_router(user_router.router, prefix="/users")
app.include_router(auth_router.router)
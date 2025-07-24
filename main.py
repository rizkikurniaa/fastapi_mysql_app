from fastapi import FastAPI
from app.routers import user
from app.database import engine
from app import models

app = FastAPI()

# Buat tabel secara otomatis
models.Base.metadata.create_all(bind=engine)

# Registrasi router
app.include_router(user.router)

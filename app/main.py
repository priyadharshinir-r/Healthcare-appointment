from fastapi import FastAPI
from app.config import engine, Base
from app.auth import router as auth_router
from app.routes import router as routes_router   


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Healthcare Management API")

app.include_router(auth_router)
app.include_router(routes_router)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:Vrdella%40123@localhost:3306/HEALTHCARE_DB"


SECRET_KEY = "secretkey123"
ALGORITHM = "HS256"
ACCESS_TOKEN_TIME_MINUTES = 15
REFRESH_TOKEN_TIME_MINUTES = 30


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

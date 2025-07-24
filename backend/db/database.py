from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO)

print("현재 작업 디렉토리:", os.getcwd())
load_dotenv('./db/.env.dev')

ID = os.getenv("ID")
PASS = os.getenv("PASS")
IP = os.getenv("IP")
PORT = os.getenv("PORT")
DBNAME = os.getenv("DBNAME")

DATABASE_URL = f"mysql+aiomysql://{ID}:{PASS}@{IP}:{PORT}/{DBNAME}"

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

# 의존성 주입용 함수
async def get_session():
    async with AsyncSessionLocal() as session:
        yield session
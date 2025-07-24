from fastapi import FastAPI, Depends
from sqlalchemy.future import select
from db.database import get_session, Base, engine
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.middleware.cors import CORSMiddleware
from db.models import get_kbo_data

app = FastAPI()

# ✅ CORS 설정 (Vue가 다른 포트에서 호출하므로 허용 필요)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],  # Vite dev 서버 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB 초기화 (테이블 생성)
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/items")
async def get_items(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(get_kbo_data))
    items = result.scalars().all()
    return items
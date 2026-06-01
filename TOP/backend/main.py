from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from config import get_settings
from routers.chat import router as chat_router

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"✅ 服務啟動 [{settings.app_env}]")
    print(f"✅ 使用模型：{settings.model_name}")
    yield
    print("🛑 服務關閉")


app = FastAPI(
    title="AI 客服系統",
    version="0.1.0",
    docs_url="/docs" if settings.app_env == "development" else None,
    redoc_url=None,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ✅ 允許所有來源
    allow_credentials=True,
    allow_methods=["*"],  # ✅ 允許所有方法（GET、POST、OPTIONS 等）
    allow_headers=["*"],  # ✅ 允許所有標頭
)

app.include_router(chat_router)
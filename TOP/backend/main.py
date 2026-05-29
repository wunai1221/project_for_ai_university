# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from config import get_settings
from routers.chat import router as chat_router

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 啟動時做的事（之後可以在這裡預載模型、向量庫）
    print(f"✅ 服務啟動 [{settings.app_env}]")
    print(f"✅ 使用模型：{settings.model_name}")
    yield
    # 關閉時做的事
    print("🛑 服務關閉")


app = FastAPI(
    title="AI 客服系統",
    version="0.1.0",
    # 正式環境關掉自動文件，避免洩漏 API 結構
    docs_url="/docs" if settings.app_env == "development" else None,
    redoc_url=None,
    lifespan=lifespan,
)

# CORS：只允許設定檔指定的來源
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "http://127.0.0.1:8080",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://192.168.0.10:8080",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(chat_router)
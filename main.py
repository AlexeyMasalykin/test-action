"""
Простое FastAPI приложение для получения текущего времени сервера
"""
from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# Создаем экземпляр приложения FastAPI
app = FastAPI(
    title="Time Server API",
    description="Простое API для получения текущего времени сервера",
    version="1.0.0"
)


class TimeResponse(BaseModel):
    """Модель ответа с текущим временем"""
    current_time: str
    timestamp: float
    timezone: str = "UTC"


@app.get("/")
async def root():
    """Корневой эндпоинт с информацией об API"""
    return {
        "message": "Time Server API",
        "endpoints": {
            "/time": "GET - получить текущее время сервера"
        }
    }


@app.get("/time", response_model=TimeResponse)
async def get_current_time():
    """
    Возвращает текущее время сервера
    
    Returns:
        TimeResponse: Объект с текущим временем, timestamp и timezone
    """
    now = datetime.utcnow()
    return TimeResponse(
        current_time=now.strftime("%Y-%m-%d %H:%M:%S"),
        timestamp=now.timestamp(),
        timezone="UTC"
    )


@app.get("/health")
async def health_check():
    """Эндпоинт для проверки работоспособности сервера"""
    return {"status": "ok", "service": "time-server"}


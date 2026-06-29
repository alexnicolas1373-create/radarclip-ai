from fastapi import FastAPI
from app.routers.auth import router as auth_router
from app.routers.trends import router as trends_router
from app.routers.process import router as process_router

app = FastAPI(title="RadarClip AI API")
app.include_router(auth_router)
app.include_router(trends_router)
app.include_router(process_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}

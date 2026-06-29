from fastapi import FastAPI
from app.routers.trends import router as trends_router

app = FastAPI(title="RadarClip AI API")
app.include_router(trends_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}

from fastapi import FastAPI

app = FastAPI(title="RadarClip AI API")

@app.get("/health")
def health_check():
    return {"status": "ok"}

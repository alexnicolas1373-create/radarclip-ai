from fastapi import APIRouter

router = APIRouter(prefix="/process", tags=["process"])


@router.post("")
def start_process():
    return {"status": "queued"}

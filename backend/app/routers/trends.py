from fastapi import APIRouter

router = APIRouter(prefix="/trends", tags=["trends"])


@router.get("")
def list_trends():
    return {"trends": []}

from fastapi import APIRouter, status


router = APIRouter(tags=["ping"])


@router.get(
    "/",
    response_model=dict(),
    status_code=status.HTTP_200_OK)
def get_ping():
    return {"message": "pong"}

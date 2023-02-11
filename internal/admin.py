from fastapi import APIRouter

router = APIRouter()


@round.post("/")
async def update_admin():
    return {"message": "Admin getting schwifty"}
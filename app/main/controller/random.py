from fastapi import APIRouter
from typing import Optional
from app.main.service.BaconIpsum import BaconIpsum

router = APIRouter()


@router.get('/random')
async def random(type: str, sentences: Optional[int] = 3):
    response = BaconIpsum(type=type, sentences=sentences).run()

    return response

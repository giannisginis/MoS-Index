from fastapi import APIRouter
from typing import Optional
from app.main.service.BaconIpsum import BaconIpsum
from app.main.utils.config import *
from app.main.Exceptions.exceptions import CustomErrorHandler

router = APIRouter()


@router.get('/random')
async def random(type: str, sentences: Optional[int] = 3):

    if type not in BaconIpsumMeta.TYPE_VALUES:
        return CustomErrorHandler(status_code=400, message=Messages.WRONG_PARAMETER_MSG)

    response = BaconIpsum(type=type, sentences=sentences).run()

    return response

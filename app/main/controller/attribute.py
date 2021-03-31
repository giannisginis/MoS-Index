from fastapi import APIRouter
from app.main.service.MOsIndex import MOsIndex

router = APIRouter()


@router.get('/attribute/')
async def get_attribute(attribute_name: str):

    response = MOsIndex().attributes2datatype()
    return response[attribute_name]
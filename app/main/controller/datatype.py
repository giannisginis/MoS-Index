from fastapi import APIRouter
from app.main.service.MOsIndex import MOsIndex

router = APIRouter()


@router.get('/datatype/')
async def get_datatype(datatype: str):
    response = MOsIndex().datatype2attributes()

    return response[datatype]

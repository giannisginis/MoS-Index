from fastapi import APIRouter
from app.main.service.MOsIndex import MOsIndex

router = APIRouter()


@router.get('/class/')
async def get_class(class_name: str):
    response = MOsIndex().class2attributes()

    return response[class_name]

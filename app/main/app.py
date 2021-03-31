from fastapi import FastAPI
from app.main.controller.attribute import router as atrributeRouter
from app.main.controller.MoClass import router as classRouter
from app.main.controller.datatype import router as datatypeRouter
from app.main.controller.random import router as randomRouter
from app.main.utils.loader import load_metadata
from app.main.Exceptions.exceptions import Exceptions


def create_app():

    app = FastAPI()
    configure_routes(app)
    event_handlers(app)
    initialize_custom_exceptions(app)

    return app


def configure_routes(app):
    app.include_router(atrributeRouter, tags=["Get parents classes and datatypes"])
    app.include_router(classRouter, tags=["Get attributes and datatypes"])
    app.include_router(datatypeRouter, tags=["Get attributes"])
    app.include_router(randomRouter, tags=["Baconipsum sequence"])


def event_handlers(app):
    @app.on_event("startup")
    async def load2cache():
        load_metadata()

    @app.on_event("shutdown")
    async def clear_cache():
        load_metadata().cache_clear()


def initialize_custom_exceptions(app):
    Exceptions(app).build_exceptions()


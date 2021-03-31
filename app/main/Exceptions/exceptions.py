from fastapi import APIRouter, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exception_handlers import (
    http_exception_handler,
)
from http.client import responses
import requests
from app.main.utils.config import Messages

errors = APIRouter()


class Exceptions:
    def __init__(self, app):
        self.app = app

    def build_exceptions(self):

        @self.app.exception_handler(RequestValidationError)
        async def validation_exception_handler(request: Request, exc: RequestValidationError):
            status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
            return JSONResponse(
                status_code=status_code,
                content=jsonable_encoder({"status_code": status_code, "detail": exc.errors(), "body": exc.body}),
            )

        @self.app.exception_handler(KeyError)
        async def custom_keyerror_exception_handler(request, exc):
            message = f"{exc} {Messages.KEY_ERROR_MESSAGE}"
            status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
            return JSONResponse(
                content=jsonable_encoder({"status_code": status_code, "detail": "key-error", "body": message}),
            )

        @self.app.exception_handler(StarletteHTTPException)
        async def custom_http_exception_handler(request, exc):
            return await http_exception_handler(request, exc)

        @self.app.exception_handler(ValueError)
        async def custom_valuerror_exception_handler(request, exc):
            message = f"{exc} {Messages.KEY_ERROR_MESSAGE}"
            status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
            return JSONResponse(
                content=jsonable_encoder(
                    {"status_code": status_code, "detail": "Value-error", "body": message}),
            )

        @self.app.exception_handler(requests.exceptions.Timeout)
        async def custom_timeout_error(request, exc):
            return JSONResponse(
                content=jsonable_encoder(
                    {"status_code": 408, "detail": "TimeoutError", "body": exc}),
            )

        @self.app.exception_handler(requests.exceptions.ConnectionError)
        async def custom_connection_error(request, exc):
            return JSONResponse(
                content=jsonable_encoder(
                    {"status_code": 408, "detail": "ConnectionError", "body": exc}),
            )


class CustomErrorHandler:
    status_code = 400

    def __init__(self, message: str = None, status_code: int = None):
        if status_code is not None:
            self.status_code = status_code
        self.message = message if message else responses[self.status_code]

    def to_dict(self):
        rv = dict()
        rv['status_code'] = self.status_code
        rv['message'] = self.message

        return rv
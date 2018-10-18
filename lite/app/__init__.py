import os
from starlette.applications import Starlette
from starlette.exceptions import ExceptionMiddleware
from starlette.middleware.wsgi import WSGIMiddleware
from starlette.routing import Router, Path, PathPrefix
import uvicorn
from wsgi import application
from .asgi_app import app as asgi_app

app = Router(
    [
        PathPrefix("/v2", app=asgi_app),
        PathPrefix("", app=WSGIMiddleware(application)),
    ]
)
DEBUG = os.getenv("DJANGO_DEBUG", "True")


if DEBUG == "True":
    app = ExceptionMiddleware(app, debug=True)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


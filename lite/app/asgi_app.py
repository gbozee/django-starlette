import os
import json
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.exceptions import ExceptionMiddleware
from starlette.background import BackgroundTask
from starlette.middleware.wsgi import WSGIMiddleware
import uvicorn
from main import print_all_models, create_record


app = Starlette()

@app.route("/")
async def homepage(request):
    alls = list(print_all_models().values("name"))
    return JSONResponse({"hello": "world", "alls": alls})


@app.route("/create", methods=["POST"])
async def signup(request):
    data = await request.json()
    name = data["name"]
    task = BackgroundTask(create_record, name=name)
    message = {"status": "Record Created"}
    return JSONResponse(message, background=task, status_code=201)




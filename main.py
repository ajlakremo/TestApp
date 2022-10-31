from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.responses import PlainTextResponse

import api

app = FastAPI()
app.include_router(api.router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)

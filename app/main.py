from fastapi import FastAPI, Request
from .db.models import Base
from .db.database import engine
from .api.v1 import routes_user, routes_contact
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.schemas.common import ErrorResponse, FieldError
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Opencredz API")

# Adicione isso antes dos `include_router`
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for e in exc.errors():
        field = ".".join(str(loc) for loc in e["loc"] if isinstance(loc, str))
        errors.append(FieldError(field=field, message=e["msg"]))
    return JSONResponse(
        status_code=422,
        content=jsonable_encoder(ErrorResponse(
            message="Validation error",
            errors=errors
        ))
    )

Base.metadata.create_all(bind=engine)

app.include_router(routes_user.router, prefix="/api/v1", tags=["Auth"])
app.include_router(routes_contact.router, prefix="/api/v1", tags=["Contact"])

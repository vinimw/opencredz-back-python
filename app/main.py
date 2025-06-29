from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from app.db.models import Base
from app.db.database import engine
from app.core.config import settings
from app.schemas.common import ErrorResponse, FieldError

from app.api.v1 import (
    routes_user,
    routes_contact,
    routes_health_plan,
    routes_financing_request,
    routes_loan_application,
    routes_loan_application_pj
)

docs_enabled = settings.ENV == "development"

app = FastAPI(
    title="Opencredz API",
    docs_url="/docs" if docs_enabled else None,
    redoc_url=None,
    openapi_url="/openapi.json" if docs_enabled else None,
)
origins = ["http://opencredz.com.br", "https://opencredz.com.br" , "https://www.opencredz.com.br", "https://opencredz-admin.netlify.app"]

if docs_enabled:
    origins = ["http://localhost:8000", "http://localhost:5173"]

# CORS (ajuste origem se necessário)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom error response
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

# Criação das tabelas (ideal separar no futuro)
Base.metadata.create_all(bind=engine)

# Rotas
app.include_router(routes_user.router, prefix="/api/v1", tags=["Auth"])
app.include_router(routes_contact.router, prefix="/api/v1", tags=["Contact"])
app.include_router(routes_health_plan.router, prefix="/api/v1", tags=["Health Plan"])
app.include_router(routes_financing_request.router, prefix="/api/v1", tags=["Financing Request"])
app.include_router(routes_loan_application.router, prefix="/api/v1", tags=["Loan Application"])
app.include_router(routes_loan_application_pj.router, prefix="/api/v1", tags=["Loan Application PJ"])

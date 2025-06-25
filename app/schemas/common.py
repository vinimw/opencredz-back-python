from pydantic import BaseModel
from typing import List, Optional

class FieldError(BaseModel):
    field: str
    message: str

class ErrorResponse(BaseModel):
    success: bool = False
    message: str
    errors: Optional[List[FieldError]] = None

class ResponseMessage(BaseModel):
    success: bool = True
    message: str

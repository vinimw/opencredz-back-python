from pydantic import BaseModel, EmailStr, constr
from typing import List
from app.schemas.common import ResponseMessage

class HealthPlanCreate(BaseModel):
    name: constr(strip_whitespace=True, min_length=2, max_length=100)
    email: EmailStr
    phone: constr(strip_whitespace=True, min_length=10, max_length=20, pattern=r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$')
    lifes: constr(strip_whitespace=True, min_length=1, max_length=3)

class HealthPlanOut(HealthPlanCreate):
    id: int

    class Config:
        from_attributes = True

class HealthPlanListResponse(ResponseMessage):
    data: List[HealthPlanOut]

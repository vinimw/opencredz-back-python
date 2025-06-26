from pydantic import BaseModel, EmailStr, constr, Field
from typing import List
from app.schemas.common import ResponseMessage

class FinancingRequestCreate(BaseModel):
    name: constr(strip_whitespace=True, min_length=2) = Field(..., alias="nome")
    cpf: constr(strip_whitespace=True, min_length=11) = Field(..., alias="cpf")
    phone: constr(strip_whitespace=True, min_length=10) = Field(..., alias="celular")
    email: EmailStr = Field(..., alias="email")
    financing_type: str = Field(..., alias="tipoFinanciamento")
    vehicle_year: str = Field(..., alias="anoVeiculo")
    vehicle_value: str = Field(..., alias="valorVeiculo")
    down_payment: str = Field(..., alias="valorEntrada")
    accepted_terms: bool = Field(..., alias="aceitaTermos")

class FinancingRequestOut(FinancingRequestCreate):
    id: int

    class Config:
        from_attributes = True
        populate_by_name = True

class FinancingRequestListResponse(ResponseMessage):
    data: List[FinancingRequestOut]

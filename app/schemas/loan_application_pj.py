from pydantic import BaseModel, EmailStr, Field
from typing import List
from app.schemas.common import ResponseMessage

from pydantic import BaseModel, Field, EmailStr, HttpUrl, constr
from typing import Optional

class LoanApplicationPJCreate(BaseModel):
    # Dados da empresa
    company_cnpj: constr(strip_whitespace=True, min_length=14) = Field(..., alias="company_cnpj")
    company_name: constr(strip_whitespace=True, min_length=2) = Field(..., alias="company_name")
    trade_name: constr(strip_whitespace=True, min_length=2) = Field(..., alias="trade_name")
    company_incorporation_date: constr(strip_whitespace=True) = Field(..., alias="company_incorporation_date")
    company_economic_activity: constr(strip_whitespace=True, min_length=2) = Field(..., alias="company_economic_activity")
    company_billing_group: constr(strip_whitespace=True, min_length=2) = Field(..., alias="company_billing_group")
    company_share_control: constr(strip_whitespace=True) = Field(..., alias="company_share_control")

    # Endereço
    zipcode: constr(strip_whitespace=True, min_length=8) = Field(..., alias="zipcode")
    address: constr(strip_whitespace=True, min_length=2) = Field(..., alias="address")
    address_number: constr(strip_whitespace=True) = Field(..., alias="address_number")
    address_complement: Optional[str] = Field("", alias="address_complement")
    neighborhood: constr(strip_whitespace=True, min_length=2) = Field(..., alias="neighborhood")
    city: constr(strip_whitespace=True, min_length=2) = Field(..., alias="city")
    state: constr(strip_whitespace=True, min_length=2, max_length=2) = Field(..., alias="state")
    country: constr(strip_whitespace=True, min_length=2) = Field(..., alias="country")

    # Contato
    phone: constr(strip_whitespace=True, min_length=10) = Field(..., alias="phone")
    fax: Optional[str] = Field("", alias="fax")
    website: Optional[str] = Field("", alias="website")
    email: EmailStr = Field(..., alias="email")

    # Sócio responsável
    responsible_name: constr(strip_whitespace=True, min_length=2) = Field(..., alias="responsible_name")
    responsible_cpf: constr(strip_whitespace=True, min_length=11) = Field(..., alias="responsible_cpf")
    responsible_rg: constr(strip_whitespace=True, min_length=5) = Field(..., alias="responsible_rg")
    responsible_birthdate: constr(strip_whitespace=True) = Field(..., alias="responsible_birthdate")
    responsible_father: constr(strip_whitespace=True, min_length=2) = Field(..., alias="responsible_father")
    responsible_mother: constr(strip_whitespace=True, min_length=2) = Field(..., alias="responsible_mother")
    marital_status: constr(strip_whitespace=True) = Field(..., alias="marital_status")
    spouse_name: Optional[str] = Field("", alias="spouse_name")
    spouse_cpf: Optional[str] = Field("", alias="spouse_cpf")

    # Veículo
    license_plate: Optional[str] = Field("", alias="license_plate")
    vehicle_type: constr(strip_whitespace=True) = Field(..., alias="vehicle_type")
    vehicle_model: constr(strip_whitespace=True, min_length=2) = Field(..., alias="vehicle_model")
    installments: constr(strip_whitespace=True) = Field(..., alias="installments")
    vehicle_year: constr(strip_whitespace=True, min_length=4) = Field(..., alias="vehicle_year")
    vehicle_year_fab: constr(strip_whitespace=True, min_length=4) = Field(..., alias="vehicle_year_fab")
    purchase_value: constr(strip_whitespace=True, min_length=3) = Field(..., alias="purchase_value")
    loan_amount: constr(strip_whitespace=True, min_length=3) = Field(..., alias="loan_amount")

class LoanApplicationPJOut(LoanApplicationPJCreate):
    id: int

    class Config:
        from_attributes = True
        populate_by_name = True

class LoanApplicationPJListResponse(ResponseMessage):
    data: List[LoanApplicationPJOut]

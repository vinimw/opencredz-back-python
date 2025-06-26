from pydantic import BaseModel, EmailStr, Field
from typing import List
from app.schemas.common import ResponseMessage

from pydantic import BaseModel, Field, EmailStr, constr

class LoanApplicationCreate(BaseModel):
    full_name: constr(strip_whitespace=True, min_length=2) = Field(..., alias="full_name")
    birth_date: constr(strip_whitespace=True) = Field(..., alias="birth_date")
    cpf_number: constr(strip_whitespace=True, min_length=11) = Field(..., alias="cpf_number")
    rg_number: constr(strip_whitespace=True, min_length=5) = Field(..., alias="rg_number")
    mother_name: constr(strip_whitespace=True, min_length=2) = Field(..., alias="mother_name")
    father_name: constr(strip_whitespace=True, min_length=2) = Field(..., alias="father_name")
    marital_status: constr(strip_whitespace=True) = Field(..., alias="marital_status")

    # Campos do cônjuge (não obrigatórios no HTML)
    spouse_name: str = Field("", alias="spouse_name")
    spouse_cpf: str = Field("", alias="spouse_cpf")

    zipcode: constr(strip_whitespace=True, min_length=8) = Field(..., alias="zipcode")
    address: constr(strip_whitespace=True, min_length=2) = Field(..., alias="address")
    address_number: constr(strip_whitespace=True) = Field(..., alias="address_number")
    address_complement: str = Field("", alias="address_complement")
    neighborhood: constr(strip_whitespace=True, min_length=2) = Field(..., alias="neighborhood")
    city: constr(strip_whitespace=True, min_length=2) = Field(..., alias="city")

    phone: constr(strip_whitespace=True, min_length=10) = Field(..., alias="phone")
    email: EmailStr = Field(..., alias="email")

    occupation: constr(strip_whitespace=True, min_length=2) = Field(..., alias="occupation")
    job_title: constr(strip_whitespace=True, min_length=2) = Field(..., alias="job_title")
    company_name: constr(strip_whitespace=True, min_length=2) = Field(..., alias="company_name")
    employer_cnpj: str = Field("", alias="employer_cnpj")  # opcional
    hire_date: constr(strip_whitespace=True) = Field(..., alias="hire_date")
    gross_monthly_income: constr(strip_whitespace=True, min_length=3) = Field(..., alias="gross_monthly_income")
    additional_income: str = Field("", alias="additional_income")
    income_source: str = Field("", alias="income_source")
    income_description: str = Field("", alias="income_description")

    license_plate_loan: str = Field("", alias="license_plate_loan")
    vehicle_type: constr(strip_whitespace=True) = Field(..., alias="vehicle_type")
    vehicle_model: constr(strip_whitespace=True, min_length=2) = Field(..., alias="vehicle_model")
    vehicle_year: constr(strip_whitespace=True) = Field(..., alias="vehicle_year")
    vehicle_year_fab: constr(strip_whitespace=True) = Field(..., alias="vehicle_year_fab")
    purchase_value: constr(strip_whitespace=True, min_length=3) = Field(..., alias="purchase_value")
    loan_amount: constr(strip_whitespace=True, min_length=3) = Field(..., alias="loan_amount")
    installments: constr(strip_whitespace=True) = Field(..., alias="installments")

    # responsável (oculto, mas obrigatório no back)
    responsible_name: str = Field("", alias="responsible_name")
    responsible_cpf: str = Field("", alias="responsible_cpf")


class LoanApplicationOut(LoanApplicationCreate):
    id: int

    class Config:
        from_attributes = True
        populate_by_name = True

class LoanApplicationListResponse(ResponseMessage):
    data: List[LoanApplicationOut]

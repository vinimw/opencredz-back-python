from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..deps import get_db, get_current_user
from ...services.dashboard_service import get_dashboard_summary
from pydantic import BaseModel

class DashboardSummary(BaseModel):
    contacts: int
    financing_request: int
    loan_application: int
    loan_applications_pj: int
    health_plans: int

router = APIRouter()

@router.get("/dashboard/summary", response_model=DashboardSummary)
def dashboard_summary(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_dashboard_summary(db)

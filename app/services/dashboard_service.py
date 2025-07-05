from sqlalchemy.orm import Session
from app.models import (
    Contact,
    FinancingRequest,
    LoanApplication,
    LoanApplicationPJ,
    HealthPlan
)

def get_dashboard_summary(db: Session):
    return {
        "contacts": db.query(Contact).count(),
        "financing_request": db.query(FinancingRequest).count(),
        "loan_application": db.query(LoanApplication).count(),
        "loan_applications_pj": db.query(LoanApplicationPJ).count(),
        "health_plans": db.query(HealthPlan).count(),
    }

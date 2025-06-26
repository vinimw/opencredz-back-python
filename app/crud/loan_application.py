from sqlalchemy.orm import Session
from typing import List
from app.models.loan_application import LoanApplication
from app.schemas.loan_application import LoanApplicationCreate

def create_loan_application(db: Session, data: LoanApplicationCreate) -> LoanApplication:
    record = LoanApplication(**data.dict(by_alias=False))
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

def get_all_loan_applications(db: Session) -> List[LoanApplication]:
    return db.query(LoanApplication).order_by(LoanApplication.id.desc()).all()

def delete_loan_application_by_id(db: Session, application_id: int) -> bool:
    record = db.query(LoanApplication).filter(LoanApplication.id == application_id).first()
    if not record:
        return False
    db.delete(record)
    db.commit()
    return True

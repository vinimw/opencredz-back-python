from sqlalchemy.orm import Session
from typing import List
from app.models.loan_application_pj import LoanApplicationPJ
from app.schemas.loan_application_pj import LoanApplicationPJCreate

def create_pj_application(db: Session, data: LoanApplicationPJCreate) -> LoanApplicationPJ:
    record = LoanApplicationPJ(**data.dict(by_alias=False))
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

def get_all_pj_applications(db: Session) -> List[LoanApplicationPJ]:
    return db.query(LoanApplicationPJ).order_by(LoanApplicationPJ.id.desc()).all()

def delete_pj_application_by_id(db: Session, application_id: int) -> bool:
    record = db.query(LoanApplicationPJ).filter(LoanApplicationPJ.id == application_id).first()
    if not record:
        return False
    db.delete(record)
    db.commit()
    return True

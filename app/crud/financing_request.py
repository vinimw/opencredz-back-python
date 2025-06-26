from sqlalchemy.orm import Session
from app.models.financing_request import FinancingRequest
from app.schemas.financing_request import FinancingRequestCreate
from typing import List

def create_request(db: Session, data: FinancingRequestCreate) -> FinancingRequest:
    record = FinancingRequest(**data.dict(by_alias=False))
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

def get_all_requests(db: Session) -> List[FinancingRequest]:
    return db.query(FinancingRequest).order_by(FinancingRequest.id.desc()).all()

def delete_request_by_id(db: Session, request_id: int) -> bool:
    record = db.query(FinancingRequest).filter(FinancingRequest.id == request_id).first()
    if not record:
        return False
    db.delete(record)
    db.commit()
    return True



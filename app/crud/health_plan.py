from sqlalchemy.orm import Session
from app.models.health_plan import HealthPlan
from app.schemas.health_plan import HealthPlanCreate
from typing import List

def create_health_plan(db: Session, plan_in: HealthPlanCreate) -> HealthPlan:
    plan = HealthPlan(**plan_in.dict())
    db.add(plan)
    db.commit()
    db.refresh(plan)
    return plan

def get_all_health_plans(db: Session) -> List[HealthPlan]:
    return db.query(HealthPlan).order_by(HealthPlan.id.desc()).all()

def delete_health_plan_by_id(db: Session, plan_id: int) -> bool:
    plan = db.query(HealthPlan).filter(HealthPlan.id == plan_id).first()
    if not plan:
        return False
    db.delete(plan)
    db.commit()
    return True

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.schemas.health_plan import HealthPlanCreate, HealthPlanOut, HealthPlanListResponse
from app.schemas.common import ResponseMessage
from app.crud import health_plan as crud_health_plan
from typing import List

router = APIRouter()

@router.post("/health-plan", response_model=ResponseMessage, status_code=status.HTTP_201_CREATED)
def create_health_plan(plan_in: HealthPlanCreate, db: Session = Depends(get_db)):
    crud_health_plan.create_health_plan(db, plan_in)
    return {
        "success": True,
        "message": "Health plan created successfully"
    }

@router.get("/health-plan", response_model=HealthPlanListResponse)
def list_health_plans(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    plans = crud_health_plan.get_all_health_plans(db)
    return {
        "success": True,
        "message": "List of health plans retrieved successfully",
        "data": plans
    }

@router.delete("/health-plan/{plan_id}", response_model=ResponseMessage)
def delete_health_plan(plan_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    deleted = crud_health_plan.delete_health_plan_by_id(db, plan_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Health plan not found")
    return {
        "success": True,
        "message": "Health plan deleted successfully"
    }

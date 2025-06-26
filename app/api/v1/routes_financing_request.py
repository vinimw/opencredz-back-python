from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.schemas.financing_request import (
    FinancingRequestCreate,
    FinancingRequestOut,
    FinancingRequestListResponse
)
from app.schemas.common import ResponseMessage
from app.crud import financing_request as crud
from typing import List

router = APIRouter()

@router.post("/financing-request", response_model=ResponseMessage, status_code=status.HTTP_201_CREATED)
def create_financing_request(data: FinancingRequestCreate, db: Session = Depends(get_db)):
    crud.create_request(db, data)
    return {
        "success": True,
        "message": "Financing request created successfully"
    }

@router.get("/financing-request", response_model=FinancingRequestListResponse)
def list_financing_requests(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    results = crud.get_all_requests(db)
    return {
        "success": True,
        "message": "List of financing requests retrieved successfully",
        "data": results
    }

@router.delete("/financing-request/{request_id}", response_model=ResponseMessage)
def delete_financing_request(request_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    deleted = crud.delete_request_by_id(db, request_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Financing request not found")
    return {
        "success": True,
        "message": "Financing request deleted successfully"
    }

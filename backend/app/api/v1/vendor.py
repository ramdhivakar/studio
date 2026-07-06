from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.vendor import VendorCreate, VendorResponse
from app.services.vendor_service import VendorService

router = APIRouter(prefix="/vendors", tags=["Vendors"])

service = VendorService()


@router.get("/", response_model=list[VendorResponse])
def get_vendors(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get("/{vendor_id}", response_model=VendorResponse)
def get_vendor(vendor_id: UUID, db: Session = Depends(get_db)):
    vendor = service.get_by_id(db, vendor_id)

    if vendor is None:
        raise HTTPException(status_code=404, detail="Vendor not found")

    return vendor


@router.post("/", response_model=VendorResponse)
def create_vendor(
    payload: VendorCreate,
    db: Session = Depends(get_db),
):
    return service.create(db, payload)


@router.delete("/{vendor_id}")
def delete_vendor(
    vendor_id: UUID,
    db: Session = Depends(get_db),
):
    vendor = service.delete(db, vendor_id)

    if vendor is None:
        raise HTTPException(status_code=404, detail="Vendor not found")

    return {"message": "Vendor deleted"}
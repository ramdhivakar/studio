from sqlalchemy.orm import Session

from app.models.vendor import Vendor


class VendorRepository:

    def get_all(self, db: Session):
        return db.query(Vendor).all()

    def get_by_id(self, db: Session, vendor_id):
        return (
            db.query(Vendor)
            .filter(Vendor.id == vendor_id)
            .first()
        )

    def create(self, db: Session, vendor: Vendor):
        db.add(vendor)
        db.commit()
        db.refresh(vendor)
        return vendor

    def delete(self, db: Session, vendor: Vendor):
        db.delete(vendor)
        db.commit()
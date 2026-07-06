from app.models.vendor import Vendor
from app.repositories.vendor_repository import VendorRepository


class VendorService:

    def __init__(self):
        self.repository = VendorRepository()

    def get_all(self, db):
        return self.repository.get_all(db)

    def get_by_id(self, db, vendor_id):
        return self.repository.get_by_id(db, vendor_id)

    def create(self, db, payload):
        vendor = Vendor(
            name=payload.name,
            description=payload.description,
        )

        return self.repository.create(db, vendor)

    def delete(self, db, vendor_id):
        vendor = self.repository.get_by_id(db, vendor_id)

        if vendor is None:
            return None

        self.repository.delete(db, vendor)

        return vendor
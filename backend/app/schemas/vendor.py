from uuid import UUID

from pydantic import BaseModel


class VendorCreate(BaseModel):
    name: str
    description: str | None = None


class VendorUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    is_active: bool | None = None


class VendorResponse(BaseModel):
    id: UUID
    name: str
    description: str | None
    is_active: bool

    model_config = {
        "from_attributes": True
    }
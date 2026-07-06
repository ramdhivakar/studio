from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.database.mixins import TimestampMixin, UUIDMixin


class ProductLine(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "product_lines"

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    vendor_id = mapped_column(
        ForeignKey("vendors.id", ondelete="CASCADE"),
        nullable=False,
    )

    vendor = relationship("Vendor", back_populates="product_lines")

    product_categories = relationship(
        "ProductCategory",
        back_populates="product_line",
        cascade="all, delete-orphan",
    )
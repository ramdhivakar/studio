from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.database.mixins import TimestampMixin, UUIDMixin


class Vendor(UUIDMixin, TimestampMixin, Base):

    __tablename__ = "vendors"

    name: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        nullable=False,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    logo_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    website_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    product_lines = relationship(
        "ProductLine",
        back_populates="vendor",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<Vendor(name='{self.name}')>"
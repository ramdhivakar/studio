from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.database.mixins import TimestampMixin, UUIDMixin


class Product(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "products"

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
        index=True,
    )

    short_name: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    description: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    category_id = mapped_column(
        ForeignKey("product_categories.id", ondelete="CASCADE"),
        nullable=False,
    )

    category = relationship(
        "ProductCategory",
        back_populates="products",
    )

    versions = relationship(
        "ProductVersion",
        back_populates="product",
        cascade="all, delete-orphan",
    )
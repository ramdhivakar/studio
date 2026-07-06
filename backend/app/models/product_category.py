from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.database.mixins import TimestampMixin, UUIDMixin


class ProductCategory(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "product_categories"

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    product_line_id = mapped_column(
        ForeignKey("product_lines.id", ondelete="CASCADE"),
        nullable=False,
    )

    product_line = relationship(
        "ProductLine",
        back_populates="product_categories",
    )

    products = relationship(
        "Product",
        back_populates="category",
        cascade="all, delete-orphan",
    )
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.database.mixins import TimestampMixin, UUIDMixin


class ProductVersion(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "product_versions"

    version: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    product_id = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE"),
        nullable=False,
    )

    product = relationship(
        "Product",
        back_populates="versions",
    )

    knowledge_articles = relationship(
        "KnowledgeArticle",
        back_populates="product_version",
        cascade="all, delete-orphan",
    )
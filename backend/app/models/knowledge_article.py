from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.database.mixins import TimestampMixin, UUIDMixin


class KnowledgeArticle(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "knowledge_articles"

    title: Mapped[str] = mapped_column(
        String(300),
        nullable=False,
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    product_version_id = mapped_column(
        ForeignKey("product_versions.id", ondelete="CASCADE"),
        nullable=False,
    )

    product_version = relationship(
        "ProductVersion",
        back_populates="knowledge_articles",
    )
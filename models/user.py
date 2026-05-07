from models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from models.item import Item


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    email_address: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(60), nullable=False)
    budget: Mapped[int] = mapped_column(Integer, nullable=False, insert_default=15000)
    items: Mapped[List["Item"]] = relationship("Item", back_populates="owner")
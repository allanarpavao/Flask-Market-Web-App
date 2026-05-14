from models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.user import User


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    barcode: Mapped[str] = mapped_column(String(12), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(1024), nullable=False, unique=True)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=True)
    owner: Mapped["User"] = relationship("User", back_populates="items")

    def buy(self, user=None):
        self.owner = user
        user.budget -= self.price

    def sell(self, user=None):
        self.owner = None
        user.budget += self.price
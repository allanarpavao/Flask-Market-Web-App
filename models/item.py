from models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    barcode: Mapped[str] = mapped_column(String(12), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(1024), nullable=False, unique=True)

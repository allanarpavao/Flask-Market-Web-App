from models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    email_address: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(60), nullable=False)

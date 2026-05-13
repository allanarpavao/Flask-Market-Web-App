from models import Base, Session
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from typing import TYPE_CHECKING, List
from extensions import bcrypt, login_manager
from flask_login import UserMixin

if TYPE_CHECKING:
    from models.item import Item

@login_manager.user_loader
def load_user(user_id):
    return Session.query(User).get(int(user_id))

class User(Base, UserMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    email_address: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(60), nullable=False)
    budget: Mapped[int] = mapped_column(Integer, nullable=False, insert_default=1000)
    items: Mapped[List["Item"]] = relationship("Item", back_populates="owner")

    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f'{self.budget}$'
    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
    
    def can_purchase(self, item_obj):
        return self.budget >= item_obj.price
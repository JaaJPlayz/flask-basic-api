from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class fruits(db.Model):
    __tablename__ = "fruits"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    price: Mapped[int] = mapped_column(Integer)
    quantity_in_stock: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(100))

    def __init__(self, name, price, quantity, description):
        self.name = name
        self.price = price
        self.quantity_in_stock = quantity
        self.description = description

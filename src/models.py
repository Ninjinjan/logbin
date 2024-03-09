from sqlalchemy import create_engine
from sqlalchemy import Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

url = "postgresql+psycopg2://ninjinjan:1@localhost:5433/logbin"

engine = create_engine(url)

class Base(DeclarativeBase):
    pass

class User(Base):

    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(40))
    email = mapped_column(String(60))
from sqlalchemy import create_engine
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)


engine = create_engine("postgresql+psycopg2://postgres:12345@localhost:5432/BankApplication")

Base.metadata.create_all(engine)

engine.dispose()
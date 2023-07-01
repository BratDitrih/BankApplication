from sqlalchemy import create_engine
from sqlalchemy import Integer, String, DECIMAL, Column, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User')
    number = Column(String, nullable=False)
    type = Column(String, nullable=False)
    currency = Column(String, nullable=False)
    amount = Column(DECIMAL, nullable=False)


engine = create_engine("sqlite:///BankApplicaton.db")

Base.metadata.create_all(engine)

engine.dispose()
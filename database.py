from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from flask import jsonify
from models import User, Account
from payment import check_and_confirm_payment

engine = create_engine("postgresql+psycopg2://postgres:12345@localhost:5432/BankApplication")


def check_user_auth(username, password):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        user = session.query(User).filter_by(username=username, password=password).first()
        if user:
            return user.id
        else:
            return None
        

def register_new_user(data):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        user = User(**data)
        session.add(user)
        session.commit()
        result = user.id
    return result


def get_user_accounts(user_id):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        accounts = session.query(Account).filter_by(user_id=user_id).all()
    return accounts

def open_account(data):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        account = Account(**data)
        session.add(account)
        session.commit()
        result = account.id
    return result


def topup_account(data):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        account = session.query(Account).filter_by(number=data['account_number']).first()
        if account:
            try:
                amount = int(data['amount'])
                if check_and_confirm_payment(data['phone_number'], amount):
                    account.amount += amount
                    session.add(account)
                    session.commit()
                    return True
            except:
                session.rollback()
    return False
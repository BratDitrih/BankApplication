from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from decimal import Decimal
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
                amount = Decimal(data['amount'])
                if check_and_confirm_payment(data['phone_number'], amount):
                    account.amount += amount
                    session.add(account)
                    session.commit()
                    return True
            except:
                session.rollback()
    return False


def transfer_money(data):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        from_account_number = data['from_account_number']
        to_account_number = data['to_account_number']
        amount = Decimal(data['amount'])
        from_account = session.query(Account).filter_by(number=from_account_number).first()
        if not from_account:
            return 'Счет с таким номером не найден'
        else:
            if from_account.amount < amount:
                return 'Недостаточно средств'
            else:
                to_account = session.query(Account).filter_by(number=to_account_number).first()
                if not to_account:
                    return 'Счет для перевода не найден'
                else:
                    try:
                        from_account.amount -= amount
                        to_account.amount += amount
                        session.add_all([from_account, to_account])
                        session.commit()
                        return 'Перевод выполнен успешно'
                    except:
                        session.rollback()
    return 'Ошибка во время перевода'
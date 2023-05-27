from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from flask import jsonify
from models import User

engine = create_engine("postgresql+psycopg2://postgres:12345@localhost:5432/BankApplication")


def check_user_auth(username, password):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        user = session.query(User).filter_by(username=username, password=password).first()
        if user:
            return True
        else:
            return False
        

def register_new_user(data):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        user = User(**data)
        session.add(user)
        session.commit()
    return jsonify({'user_id': user.id})
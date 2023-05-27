from flask import Flask, render_template, request, redirect, abort, jsonify
import database
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user_id =  database.check_user_auth(username, password)
    if user_id:
        return jsonify({'user_id': user_id})
    else:
        return abort(401)
    

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')
    phone = request.json.get('phone')
    
    data = {'username': username, 'password': password, 'email': email, 'phone': phone}
    user_id = database.register_new_user(data)
    if user_id:
        return jsonify({'user_id': user_id})
    else:
        return abort(401)
    

@app.route('/account/open', methods=['POST'])
def open_account():
    user_id = request.json.get('userId')
    digits = []
    for i in range(4):
        digits.append(str(random.randint(1000, 9999)))
    number = ' '.join(digits)
    type = request.json.get('type')
    amount = 0

    data = {'user_id': user_id, 'number': number, 'type': type, 'amount': amount}
    account_id = database.open_account(data)
    if account_id:
        return jsonify({'account_id': account_id})
    else:
        return jsonify({'error': 'Не удалось открыть счет'}), 500


@app.route('/user/<int:user_id>')
def user_profile(user_id):
    user_accounts = database.get_user_accounts(user_id)
    return render_template('user_profile.html', user_id=user_id, accounts=user_accounts)


if __name__ == '__main__':
    app.run(debug=True)
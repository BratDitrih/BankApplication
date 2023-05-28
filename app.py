from flask import Flask, render_template, request, abort, jsonify
import database
import random

app = Flask(__name__)


@app.before_request
def check_referer():
    referer = request.referrer
    if request.path != '/' and referer is None:
        return abort(403)


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
    
    data = {
        'username': username, 
        'password': password, 
        'email': email, 
        'phone': phone
        }
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

    data = {
        'user_id': user_id, 
        'number': number, 
        'type': type,
        'amount': amount
        }
    account_id = database.open_account(data)
    if account_id:
        return jsonify({'account_id': account_id})
    else:
        return jsonify({'error': 'Не удалось открыть счет'}), 500
    

@app.route('/account/topup', methods=['POST'])
def topup_account():
    account_number = request.json.get('accountNumber')
    phone_number = request.json.get('phoneNumber')
    amount = request.json.get('amount')

    data = {
        'account_number': account_number, 
        'phone_number': phone_number, 
        'amount': amount
        }
    success = database.topup_account(data)
    if success:
        return jsonify({'status': 'Счет успешно пополнен'})
    else:
        return jsonify({'error': 'Не удалось пополнить счет'}), 500
    

@app.route('/account/transfer', methods=['POST'])
def transfer_money():
    from_account_number = request.json.get('fromAccountNumber')
    to_account_number = request.json.get('toAccountNumber')
    amount = request.json.get('amount')

    data = {
        'from_account_number': from_account_number, 
        'to_account_number': to_account_number, 
        'amount': amount
        }
    success = database.transfer_money(data)
    if success == 'Перевод выполнен успешно':
        return jsonify({'status': 'Перевод выполнен успешно'})
    elif success == 'Недостаточно средств':
        return jsonify({'status': 'Недостаточно средств'})
    elif success == 'Счет для перевода не найден':
        return jsonify({'status': 'Счет для перевода не найден'})
    else:
        return jsonify({'error': 'Не удалось перевести деньги'}), 500


@app.route('/user/<int:user_id>', methods=['GET'])
def user_profile(user_id):
    user_accounts = database.get_user_accounts(user_id)
    return render_template('user_profile.html', user_id=user_id, accounts=user_accounts)


if __name__ == '__main__':
    app.run(debug=True)
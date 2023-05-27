from flask import Flask, render_template, request, redirect, abort
import database

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if database.check_user_auth(username, password):
        return redirect('/dashboard')
    else:
        return abort(401)
    

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')
    phone = request.json.get('phone')
    
    data = {'username': username, 'password': password, 'email': email, 'phone': phone}
    result = database.register_new_user(data)
    return result


@app.route('/dashboard')
def dashboard():
    return 'Добро пожаловать!'


if __name__ == '__main__':
    app.run(debug=True)
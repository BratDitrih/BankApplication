def check_and_confirm_payment(phone_number, amount):
    balance = get_balance(phone_number)

    if balance < amount:
        return False

    confirmation_code = send_confirmation_message(phone_number, amount)

    if confirm_payment(confirmation_code):
        make_payment(phone_number, amount)
        return True
    else:
        return False

def get_balance(phone_number):
    balance = 100_000
    return balance

def send_confirmation_message(phone_number, amount):
    confirmation_code = '1234'
    return confirmation_code

def confirm_payment(confirmation_code):
    if confirmation_code == '1234':
        return True
    else:
        return False

def make_payment(phone_number, amount):
    pass

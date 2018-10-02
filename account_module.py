# Begin account_module.py
balance = 0


def deposit(amount):
    global balance
    balance += amount


def withdraw(amount):
    global balance
    balance += (-amount)


def check():
    global balance
    return balance


# End account_module.py

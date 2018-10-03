
# Begin account_module.py

balance = 0


def deposit(amount):
    global balance
    print(f"deposit {amount}")
    balance += amount


def withdraw(amount):
    global balance
    print(f"withdraw {amount}")
    balance += (-amount)


def check():
    global balance
    return balance


# End account_module.py

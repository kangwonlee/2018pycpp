balance = 0

def deposit(amount):
    balance += amount

def withdraw(amount):
    balance += (-amount)

def check():
    return balance


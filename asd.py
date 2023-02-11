import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


def retrieve_balance(name):
    with open("balance.txt", "r") as f:
        for line in f:
            account = line.strip().split(":")
            if account[0] == name:
                return int(account[1])
    return None

def add_balance(name, amount):
    with open("balance.txt", "a") as f:
        f.write("{}:{}\n".format(name, amount))

def update_balance(name, amount):
    accounts = []
    found = False
    with open("balance.txt", "r") as f:
        for line in f:
            account = line.strip().split(":")
            if account[0] == name:
                found = True
                accounts.append("{}:{}".format(name, str(int(account[1]) + amount)))
            else:
                accounts.append(line.strip())
    if found:
        with open("balance.txt", "w") as f:
            for account in accounts:
                f.write("{}\n".format(account))

def init_ui(self):
    self.setWindowTitle("Bank Account Manager")

    #Account Name Imput
    self.account_name_input = QLineEdit()
    self.account_name_input.setPlaceholderText("Enter Account Name")

name = input("Enter the account holder's name: ")
amount = retrieve_balance(name)
if amount:
    print("The balance for {} is {}".format(name, amount))
    action = input("Would you like to (w)ithdraw or (d)eposit money? ")
    if action.lower() == "w":
        withdraw = int(input("Enter the amount you want to withdraw: "))
        if amount - withdraw >= 0:
            update_balance(name, -withdraw)
            print("{} has been withdrawn from {}'s account.".format(withdraw, name))
            print("The new balance is {}".format(retrieve_balance(name)))
        else:
            print("Insufficient funds.")
    elif action.lower() == "d":
        deposit = int(input("Enter the amount you want to deposit: "))
        update_balance(name, deposit)
        print("{} has been deposited into {}'s account.".format(deposit, name))
        print("The new balance is {}".format(retrieve_balance(name)))
    else:
        print("Invalid action.")
else:
    print("No account found for {}".format(name))
    add = input("Would you like to add an account for {}? (yes/no) ".format(name))
    if add.lower() == "yes":
        amount = int(input("Enter the starting balance for {}: ".format(name)))
        add_balance(name, amount)
        print("An account for {} with a starting balance of {} has been added.".format(name, amount))
    else:
        print("An account for {} has not been added.".format(name))

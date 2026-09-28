import random
from datetime import datetime

# Store all accounts
accounts = {}


# -------------------------------
# Generate Account Number
# -------------------------------
def generate_account_number():
    while True:
        account_number = random.randint(100000, 999999)

        if account_number not in accounts:
            return account_number


# -------------------------------
# Create Account
# -------------------------------
def create_account():
    print("\n========== CREATE ACCOUNT ==========")

    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")

    while True:
        pin = input("Create a 4-digit PIN: ")

        if len(pin) == 4 and pin.isdigit():
            break

        print("PIN must contain exactly 4 digits.")

    account_number = generate_account_number()

    accounts[account_number] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0.0,
        "transactions": []
    }

    print("\nAccount created successfully!")
    print("Your Account Number is:", account_number)
    print("Please remember your Account Number and PIN.")


# -------------------------------
# Login
# -------------------------------
def login():
    print("\n========== LOGIN ==========")

    try:
        account_number = int(input("Enter Account Number: "))
    except ValueError:
        print("Invalid account number.")
        return

    pin = input("Enter PIN: ")

    if account_number in accounts:

        if accounts[account_number]["pin"] == pin:
            print("\nLogin successful!")
            print("Welcome,", accounts[account_number]["name"])

            account_menu(account_number)

        else:
            print("Incorrect PIN.")

    else:
        print("Account not found.")


# -------------------------------
# Check Balance
# -------------------------------
def check_balance(account_number):
    balance = accounts[account_number]["balance"]

    print("\n========== BALANCE ==========")
    print("Current Balance: ₹{:.2f}".format(balance))


# -------------------------------
# Deposit Money
# -------------------------------
def deposit(account_number):
    print("\n========== DEPOSIT ==========")

    try:
        amount = float(input("Enter amount to deposit: "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    accounts[account_number]["balance"] += amount

    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    accounts[account_number]["transactions"].append(
        f"{time} - Deposited ₹{amount:.2f}"
    )

    print("₹{:.2f} deposited successfully.".format(amount))
    print("New Balance: ₹{:.2f}".format(
        accounts[account_number]["balance"]
    ))


# -------------------------------
# Withdraw Money
# -------------------------------
def withdraw(account_number):
    print("\n========== WITHDRAW ==========")

    try:
        amount = float(input("Enter amount to withdraw: "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    if amount > accounts[account_number]["balance"]:
        print("Insufficient balance.")
        return

    accounts[account_number]["balance"] -= amount

    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    accounts[account_number]["transactions"].append(
        f"{time} - Withdrawn ₹{amount:.2f}"
    )

    print("₹{:.2f} withdrawn successfully.".format(amount))
    print("Remaining Balance: ₹{:.2f}".format(
        accounts[account_number]["balance"]
    ))


# -------------------------------
# Transfer Money
# -------------------------------
def transfer(account_number):
    print("\n========== TRANSFER MONEY ==========")

    try:
        receiver = int(input("Enter receiver Account Number: "))
    except ValueError:
        print("Invalid account number.")
        return

    if receiver not in accounts:
        print("Receiver account not found.")
        return

    if receiver == account_number:
        print("You cannot transfer money to your own account.")
        return

    try:
        amount = float(input("Enter amount to transfer: "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    if amount > accounts[account_number]["balance"]:
        print("Insufficient balance.")
        return

    # Deduct money from sender
    accounts[account_number]["balance"] -= amount

    # Add money to receiver
    accounts[receiver]["balance"] += amount

    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Sender transaction
    accounts[account_number]["transactions"].append(
        f"{time} - Transferred ₹{amount:.2f} to Account {receiver}"
    )

    # Receiver transaction
    accounts[receiver]["transactions"].append(
        f"{time} - Received ₹{amount:.2f} from Account {account_number}"
    )

    print("\nTransfer successful!")
    print("Amount transferred: ₹{:.2f}".format(amount))
    print("Receiver Account:", receiver)
    print("Remaining Balance: ₹{:.2f}".format(
        accounts[account_number]["balance"]
    ))


# -------------------------------
# Transaction History
# -------------------------------
def transaction_history(account_number):
    print("\n========== TRANSACTION HISTORY ==========")

    transactions = accounts[account_number]["transactions"]

    if len(transactions) == 0:
        print("No transactions available.")
        return

    for transaction in transactions:
        print(transaction)


# -------------------------------
# Change PIN
# -------------------------------
def change_pin(account_number):
    print("\n========== CHANGE PIN ==========")

    old_pin = input("Enter your old PIN: ")

    if old_pin != accounts[account_number]["pin"]:
        print("Incorrect old PIN.")
        return

    while True:
        new_pin = input("Enter new 4-digit PIN: ")

        if len(new_pin) == 4 and new_pin.isdigit():
            break

        print("PIN must contain exactly 4 digits.")

    confirm_pin = input("Confirm new PIN: ")

    if new_pin != confirm_pin:
        print("PINs do not match.")
        return

    accounts[account_number]["pin"] = new_pin

    print("PIN changed successfully!")


# -------------------------------
# Account Menu
# -------------------------------
def account_menu(account_number):

    while True:

        print("\n================================")
        print("         ACCOUNT MENU")
        print("================================")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Change PIN")
        print("7. Logout")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(account_number)

        elif choice == "2":
            deposit(account_number)

        elif choice == "3":
            withdraw(account_number)

        elif choice == "4":
            transfer(account_number)

        elif choice == "5":
            transaction_history(account_number)

        elif choice == "6":
            change_pin(account_number)

        elif choice == "7":
            print("\nLogged out successfully.")
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice. Please try again.")


# -------------------------------
# Main Menu
# -------------------------------
def main():

    while True:

        print("\n========================================")
        print("          BANKING SYSTEM")
        print("========================================")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            login()

        elif choice == "3":
            print("\nThank you for using Banking System!")
            break

        else:
            print("Invalid choice. Please try again.")


# -------------------------------
# Start Program
# -------------------------------
if __name__ == "__main__":
    main()
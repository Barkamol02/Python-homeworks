import json
import os

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def to_dict(self):
        return {"account_number": self.account_number, "name": self.name, "balance": self.balance}

    @classmethod
    def from_dict(cls, data):
        return cls(data["account_number"], data["name"], data["balance"])

    def __str__(self):
        return f"Account({self.account_number}): {self.name} - Balance: ${self.balance:.2f}"


class Bank:
    def __init__(self, file="accounts.json"):
        self.file = file
        self.accounts = self.load_from_file()
        self.number = max(self.accounts.keys(), default=1000) + 1 

    def create_account(self, name, initial_deposit):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string!")
        if not isinstance(initial_deposit, (int, float)) or initial_deposit < 0:
            raise ValueError("Initial deposit must be a positive number!")

        acc_number = self.number
        self.number += 1
        account = Account(acc_number, name, initial_deposit)
        self.accounts[acc_number] = account
        self.save_to_file()
        print(f"Account created successfully! Your account number is {acc_number}")

    def view_account(self, account_number):
        account_number = self.validate_account_number(account_number)
        return self.accounts[account_number]

    def deposit(self, account_number, amount):
        account_number = self.validate_account_number(account_number)
        amount = self.validate_amount(amount)

        self.accounts[account_number].balance += amount
        self.save_to_file()
        print(f"Deposited ${amount:.2f} successfully. New balance: ${self.accounts[account_number].balance:.2f}")

    def withdraw(self, account_number, amount):
        account_number = self.validate_account_number(account_number)
        amount = self.validate_amount(amount)

        if amount > self.accounts[account_number].balance:
            raise ValueError("Insufficient funds!")
        
        self.accounts[account_number].balance -= amount
        self.save_to_file()
        print(f"Withdrew ${amount:.2f} successfully. New balance: ${self.accounts[account_number].balance:.2f}")

    def validate_account_number(self, account_number):
        """Ensures the account number is valid."""
        if not isinstance(account_number, int):
            raise ValueError("Account number should be an integer!")
        if account_number not in self.accounts:
            raise ValueError("Account number not found!")
        return account_number

    def validate_amount(self, amount):
        """Ensures the deposit/withdrawal amount is valid."""
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be a positive number!")
        return amount

    def save_to_file(self):
        """Saves all accounts to a JSON file."""
        try:
            with open(self.file, "w") as file:
                json.dump({acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}, file, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_from_file(self):
        """Loads accounts from a JSON file or returns an empty dictionary if not found."""
        if not os.path.exists(self.file):
            return {}

        try:
            with open(self.file, "r") as file:
                data = json.load(file)
                return {int(acc_num): Account.from_dict(acc_data) for acc_num, acc_data in data.items()}
        except (json.JSONDecodeError, FileNotFoundError):
            return {}


if __name__ == "__main__":
    bank = Bank()

    
    try:
        bank.create_account("Alice", 500)
        bank.create_account("Bob", 1000)
    except ValueError as e:
        print(f"Error: {e}")

  
    try:
        print(bank.view_account(1000))
        print(bank.view_account(1001))
    except ValueError as e:
        print(f"Error: {e}")

    try:
        bank.deposit(1000, 200)
    except ValueError as e:
        print(f"Error: {e}")

    
    try:
        bank.withdraw(1001, 300)
    except ValueError as e:
        print(f"Error: {e}")

    
    try:
        bank.withdraw(1000, -50) 
    except ValueError as e:
        print(f"Error: {e}")

    try:
        bank.deposit(9999, 100) 
    except ValueError as e:
        print(f"Error: {e}")

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional starting balance (default = 0)."""
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if sufficient balance exists. Returns True if success, False otherwise."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
    """Display the current balance with 2 decimal places."""
    print(f"Current Balance: ${self.__account_balance:.2f}")


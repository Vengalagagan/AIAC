class BankAccount:
    
    def __init__(self, name, balance=0):
       
        if not name or not name.strip():
            raise ValueError("Account holder name cannot be empty")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
            
        # Initialize instance attributes
        self.name = name.strip()  # Remove leading/trailing whitespace
        self.balance = float(balance)  # Ensure balance is a float

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        # Add amount to balance
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds. Available: ${self.balance:.2f}, Requested: ${amount:.2f}")
        
        # Subtract amount from balance
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        return self.balance

    def get_balance(self):
        return self.balance
    
    def display_account_info(self):
        print("=" * 40)
        print("ACCOUNT INFORMATION")
        print("=" * 40)
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: ${self.balance:.2f}")
        print("=" * 40)
if __name__ == "__main__":

    print("BankAccount Class Demonstration")
    print("=" * 50)
    
    try:
        # Create a new bank account
        print("\n1. Creating a new bank account...")
        account1 = BankAccount("John Doe", 1000.00)
        account1.display_account_info()
        
        # Demonstrate deposit operations
        print("\n2. Performing deposit operations...")
        account1.deposit(500.00)  # Valid deposit
        account1.deposit(250.50)  # Another valid deposit
        
        # Demonstrate withdrawal operations
        print("\n3. Performing withdrawal operations...")
        account1.withdraw(200.00)  # Valid withdrawal
        account1.withdraw(100.25)  # Another valid withdrawal
        
        # Check balance
        print(f"\n4. Current balance: ${account1.get_balance():.2f}")
        
        # Display final account information
        print("\n5. Final account status:")
        account1.display_account_info()
        
        # Demonstrate error handling
        print("\n6. Testing error handling...")
        try:
            account1.deposit(-100)  # Invalid deposit
        except ValueError as e:
            print(f"Error caught: {e}")
            
        try:
            account1.withdraw(2000)  # Insufficient funds
        except ValueError as e:
            print(f"Error caught: {e}")
            
        # Create another account with different initial balance
        print("\n7. Creating another account...")
        account2 = BankAccount("Jane Smith", 500.00)
        account2.display_account_info()
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    print("\n" + "=" * 50)
    print("Demonstration completed successfully!")
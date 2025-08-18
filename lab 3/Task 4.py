import re
import hashlib
import json
import datetime
from typing import Dict, Optional, Tuple
class UserDatabase:
    def __init__(self, filename: str = "users.json"):
        self.filename = filename
        self.users = self._load_users()
    
    def _load_users(self) -> Dict[str, Dict]:
        """Load users from JSON file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def _save_users(self):
        """Save users to JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.users, file, indent=2)
    
    def add_user(self, username: str, password_hash: str, email: str) -> bool:
        """Add a new user to the database."""
        if username in self.users:
            return False
        
        self.users[username] = {
            'password_hash': password_hash,
            'email': email,
            'created_at': str(datetime.datetime.now())
        }
        self._save_users()
        return True
    
    def verify_user(self, username: str, password_hash: str) -> bool:
        """Verify user credentials."""
        if username not in self.users:
            return False
        return self.users[username]['password_hash'] == password_hash
    
    def get_user_info(self, username: str) -> Optional[Dict]:
        """Get user information."""
        return self.users.get(username)


def hash_password(password: str) -> str:
    """Hash password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def validate_username(username: str) -> Tuple[bool, str]:
    """Validate username format."""
    if len(username) < 3:
        return False, "Username must be at least 3 characters long"
    if len(username) > 20:
        return False, "Username must be less than 20 characters long"
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return False, "Username can only contain letters, numbers, and underscores"
    return True, ""


def validate_password(password: str) -> Tuple[bool, str]:
    """Validate password strength."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search(r'\d', password):
        return False, "Password must contain at least one number"
    return True, ""


def validate_email(email: str) -> Tuple[bool, str]:
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        return False, "Invalid email format"
    return True, ""


def register_user(username: str, password: str, email: str) -> Tuple[bool, str]:
    username_valid, username_msg = validate_username(username)
    if not username_valid:
        return False, f"Username validation failed: {username_msg}"
    
    password_valid, password_msg = validate_password(password)
    if not password_valid:
        return False, f"Password validation failed: {password_msg}"
    
    email_valid, email_msg = validate_email(email)
    if not email_valid:
        return False, f"Email validation failed: {email_msg}"
    
    # Hash the password
    password_hash = hash_password(password)
    if user_db.add_user(username, password_hash, email):
        return True, f"User '{username}' registered successfully!"
    else:
        return False, f"Username '{username}' already exists"


def login_user(username: str, password: str) -> Tuple[bool, str]:
    if not username or not password:
        return False, "Username and password are required"
    password_hash = hash_password(password)
    if user_db.verify_user(username, password_hash):
        user_info = user_db.get_user_info(username)
        return True, f"Login successful! Welcome back, {username}"
    else:
        return False, "Invalid username or password"
def main():
    """Main function to demonstrate the authentication system."""
    print("=== User Authentication System ===\n")
    
    while True:
        print("1. Register new user")
        print("2. Login existing user")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            print("\n--- User Registration ---")
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            email = input("Enter email: ").strip()
            
            success, message = register_user(username, password, email)
            print(f"Result: {message}\n")
            
        elif choice == "2":
            print("\n--- User Login ---")
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            
            success, message = login_user(username, password)
            print(f"Result: {message}\n")
            
        elif choice == "3":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")
user_db = UserDatabase()
if __name__ == "__main__":
    main()

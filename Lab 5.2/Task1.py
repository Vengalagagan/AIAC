import json
import os
import base64
import getpass
import hashlib
import hmac
import secrets
from typing import Dict, Any


USERS_DB_FILE = "users.json"
HASH_ALGORITHM = "sha256"
PBKDF2_ITERATIONS = 200_000
SALT_NUM_BYTES = 16


def _load_users_db() -> Dict[str, Any]:
    if not os.path.exists(USERS_DB_FILE):
        return {"users": {}}
    try:
        with open(USERS_DB_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        # If file is corrupted or empty, initialize a new structure
        return {"users": {}}


def _save_users_db(db: Dict[str, Any]) -> None:
    temp_path = USERS_DB_FILE + ".tmp"
    with open(temp_path, "w", encoding="utf-8") as file:
        json.dump(db, file, indent=2)
    # Atomic-ish replace on Windows
    if os.path.exists(USERS_DB_FILE):
        os.replace(temp_path, USERS_DB_FILE)
    else:
        os.rename(temp_path, USERS_DB_FILE)


def _derive_password_hash(password: str, salt: bytes, iterations: int = PBKDF2_ITERATIONS) -> bytes:
    return hashlib.pbkdf2_hmac(HASH_ALGORITHM, password.encode("utf-8"), salt, iterations)


def create_account() -> None:
    db = _load_users_db()
    users = db.setdefault("users", {})

    username = input("Choose a username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return
    if username in users:
        print("That username is already taken.")
        return

    password = getpass.getpass("Choose a password: ")
    confirm = getpass.getpass("Confirm password: ")
    if password != confirm:
        print("Passwords do not match.")
        return
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return

    salt = secrets.token_bytes(SALT_NUM_BYTES)
    pwd_hash = _derive_password_hash(password, salt)

    users[username] = {
        "salt_b64": base64.b64encode(salt).decode("ascii"),
        "hash_b64": base64.b64encode(pwd_hash).decode("ascii"),
        "iterations": PBKDF2_ITERATIONS,
        "algorithm": f"pbkdf2_{HASH_ALGORITHM}",
    }

    _save_users_db(db)
    print("Account created successfully.")


def login() -> None:
    db = _load_users_db()
    users = db.get("users", {})

    username = input("Username: ").strip()
    if username not in users:
        print("Invalid username or password.")
        return

    user_record = users[username]
    try:
        salt = base64.b64decode(user_record["salt_b64"])  # type: ignore[index]
        expected_hash = base64.b64decode(user_record["hash_b64"])  # type: ignore[index]
        iterations = int(user_record.get("iterations", PBKDF2_ITERATIONS))
    except Exception:
        print("User record is corrupted.")
        return

    password = getpass.getpass("Password: ")
    computed_hash = _derive_password_hash(password, salt, iterations)

    if hmac.compare_digest(computed_hash, expected_hash):
        print(f"Welcome, {username}!")
    else:
        print("Invalid username or password.")


def main() -> None:
    actions = {
        "1": ("Create account", create_account),
        "2": ("Login", login),
        "3": ("Exit", None),
    }

    while True:
        print("\n=== Secure Login System ===")
        for key, (label, _) in actions.items():
            print(f"{key}. {label}")

        choice = input("Choose an option: ").strip()
        if choice == "3":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid choice.")
            continue
        _, func = action
        if func is not None:
            func()


if __name__ == "__main__":
    main()



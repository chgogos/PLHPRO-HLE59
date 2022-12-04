import hashlib
from getpass import getpass

user_password_dict = {}


def hash_password(plain_password):
    return hashlib.sha224(plain_password.encode("UTF-8")).hexdigest()


def new_user():
    pass


def update_password():
    pass


def login():
    pass


def display_users():
    pass


if __name__ == "__main__":
    while True:
        print("1. εγγραφή 2. ενημέρωση συνθηματικού 3. είσοδος 4. λίστα χρηστών")
        choice = input("Εισάγετε την επιλογή σας: ")
        if choice == "":
            break
        elif choice == "1":
            new_user()
        elif choice == "2":
            update_password()
        elif choice == "3":
            login()
        elif choice == "4":
            display_users()

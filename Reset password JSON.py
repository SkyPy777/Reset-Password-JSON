

import json

user_data = {}

def load_data():
    try:
        with open('user_data.json', 'r') as file:
            user_data.update(json.load(file))
        print("User data loaded")
    except FileNotFoundError:
        print("User data not found")

def save_data():
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)
    print("User data saved.")

def register():
    username = input("\nEnter a new username: ")
    if username in user_data:
        print("Username already exists.")
    else:
        password = input("\nEnter a password: ")
        user_data[username] = password
        save_data()
        print("\nRegistration successful.")

def reset_password():
    if not user_data:
        print("\nUser is not registered.")
        return

    username = input("\nEnter your username: ")

    if username in user_data:
        current_password = input("\nEnter your current password: ")  

        if user_data[username] == current_password:
            new_password = input("Enter your new password: ")  
            user_data[username] = new_password  
            save_data()
            print("\nPassword reset successfully.")
        else:
            print("\nCurrent password is incorrect.")
    else:
        print("\nPlease enter a valid username.")

while True:
    print("\nWelcome to the password management system:")
    print("1. Register")
    print("2. Reset Password")
    print("3. Exit")

    choice = input("\nEnter the choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        reset_password()
    elif choice == "3":
        break
    else:
        print("\nEnter a valid option.")


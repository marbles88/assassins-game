import requests
import json

# Base URL of your Flask application
BASE_URL = "http://127.0.0.1:5000"

def add_user(name, username, password):
    """Add a new user to the database."""
    response = requests.post(f"{BASE_URL}/add_user", json={
        "name": name,
        "username": username,
        "password": password
    })
    # print("Status Code:", response.status_code) #debug
    # print("Raw Response:", response.text)
    try:
        return response.json()
    except json.JSONDecodeError:
        print("Could not decode JSON response")
        return None

def get_all_users():
    """Retrieve all users from the database."""
    response = requests.get(f"{BASE_URL}/users")
    return response.json()

def remove_user(user_id):
    """Remove a user from the database by ID."""
    response = requests.delete(f"{BASE_URL}/remove_user/{user_id}")
    print(response.json())

def print_users(users):
    """Print user information in a formatted way."""
    print("Current Users:")
    for user in users:
        print(f"ID: {user['id']}, Name: {user['name']}, Username: {user['username']}")
    print()

# Interactive menu
while True:
    print("\n1. Add User")
    print("2. View All Users")
    print("3. Remove User")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        name = input("Enter name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        result = add_user(name, username, password)
        if result:
            print("Server response:", result)
        else:
            print("Failed to add user")
    elif choice == '2':
        users = get_all_users()
        print_users(users)
    elif choice == '3':
        user_id = input("Enter user ID to remove: ")
        remove_user(user_id)
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
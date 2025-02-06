import json
import os
import re

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Corrupted contacts file. Starting fresh.")
            return {}
    return {}
    
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def validate_phone(phone):
    return re.fullmatch(r"\d{7,15}", phone) is not None

def validate_email(email):
    return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email) is not None

def add_contact():
    contacts = load_contacts()

    name = input("Enter name: ").strip().lower()
    if not name:
        print("Error: Name cannot be empty!")
        return

    if name in contacts:
        print("Error: Contact already exists!")
        return

    phone = input("Enter phone number: ").strip()
    if not validate_phone(phone):
        print("Error: Invalid phone number! Must be 7-15 digits.")
        return

    email = input("Enter email: ").strip()
    if not validate_email(email):
        print("Error: Invalid email format!")
        return

    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print("Contact added successfully!")

def search_contact():
    contacts = load_contacts()
    name = input("Enter name to search: ").strip().lower()

    if name in contacts:
        contact = contacts[name]
        print(f"\n Contact Found:")
        print(f"Name: {name.capitalize()}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}\n")
    else:
        print(" Contact not found.")

def update_contact():
    contacts = load_contacts()
    name = input("Enter name to update: ").strip().lower()

    if name in contacts:
        print(f" Updating Contact: {name.capitalize()}")
        print(f"Current Phone: {contacts[name]['phone']}")
        print(f"Current Email: {contacts[name]['email']}")

        phone = input("Enter new phone (press Enter to keep current): ").strip()
        if phone and not validate_phone(phone):
            print("Error: Invalid phone number!")
            return

        email = input("Enter new email (press Enter to keep current): ").strip()
        if email and not validate_email(email):
            print("Error: Invalid email format!")
            return

        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email

        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\n Contact Management System")
        print("1️  Add Contact")
        print("2️  Search Contact")
        print("3️  Update Contact")
        print("4️  Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)
        file.flush()  # Ensure data is written immediately


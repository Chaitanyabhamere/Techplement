import json
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Corrupted contacts file.")
            return {}
    return {}


def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("📂 No contacts found.")
        return

    print("\n📄 Contact List:")
    for name, details in contacts.items():
        print(f"👤 Name: {name.capitalize()}\n📞 Phone: {details['phone']}\n📧 Email: {details['email']}\n")


# Call the function to test it
view_contacts()

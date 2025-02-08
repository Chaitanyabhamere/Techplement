import json
import os
CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            data = file.read().strip()
            return json.loads(data) if data else {}
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    contacts = load_contacts()
    name = input("Enter name: ").strip().lower()
    if not name or name in contacts:
        return print("Invalid or duplicate name!")
    contacts[name] = {
        "phone": input("Enter phone number: ").strip(),
        "email": input("Enter email: ").strip()
    }
    save_contacts(contacts)
    print("Contact added successfully!")

def search_contact():
    contacts = load_contacts()
    name = input("Enter name to search: ").strip().lower()

    contact = contacts.get(name)
    if not contact:
        return print("Contact not found.")

    print(f"\nContact Found: {name.capitalize()} (Phone: {contact['phone']}, Email: {contact['email']})")

def update_contact():
    contacts = load_contacts()
    name = input("Enter name to update: ").strip().lower()

    if name not in contacts:
        return print("Contact not found.")

    print(f"Updating {name.capitalize()} (Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']})")

    contacts[name]["phone"] = input("New phone (Enter to keep current): ").strip() or contacts[name]["phone"]
    contacts[name]["email"] = input("New email (Enter to keep current): ").strip() or contacts[name]["email"]

    save_contacts(contacts)
    print("Contact updated successfully!")

def delete_contact():
    contacts = load_contacts()
    name = input("Enter name to delete: ").strip().lower()

    if name not in contacts:
        return print("Contact not found.")

    contacts.pop(name)
    save_contacts(contacts)
    print("Contact deleted successfully!")

def main():
    while True:
        print("\nContact Manager")
        print("1️ Add Contact")
        print("2️ Search Contact")
        print("3️ Update Contact")
        print("4️ Delete Contact")
        print("5️ Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

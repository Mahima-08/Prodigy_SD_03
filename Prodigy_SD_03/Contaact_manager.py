import json

def load_contacts(filename="contacts.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts, filename="contacts.json"):
    with open(filename, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"Contact for {name} added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"\nName: {name}\nPhone: {info['Phone']}\nEmail: {info['Email']}")

def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ")
    if name in contacts:
        phone = input(f"Enter the new phone number (current: {contacts[name]['Phone']}): ")
        email = input(f"Enter the new email address (current: {contacts[name]['Email']}): ")
        contacts[name] = {"Phone": phone, "Email": email}
        print(f"Contact for {name} updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact for {name} deleted successfully.")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()

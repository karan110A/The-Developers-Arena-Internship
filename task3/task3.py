# -------------------------------------------
# Contact Management System
# -------------------------------------------

# Dictionary to store contacts
# Format: {"Alice": "1234567890", "Bob": "9876543210"}
contacts = {}


# -------------------------------------------
# Function: Add a contact
# -------------------------------------------
def add_contact(name, phone):
    """
    Adds a new contact to the contacts dictionary.
    name: string
    phone: string
    """
    contacts[name] = phone
    print(f"✔ Contact '{name}' added successfully!")


# -------------------------------------------
# Function: Search for a contact
# -------------------------------------------
def search_contact(name):
    """
    Searches for a contact by name.
    Returns phone number if found, otherwise None.
    """
    if name in contacts:
        print(f"📞 {name}'s number is: {contacts[name]}")
        return contacts[name]
    else:
        print(f"❌ Contact '{name}' not found.")
        return None


# -------------------------------------------
# Function: Display all contacts
# -------------------------------------------
def display_contacts():
    """
    Displays all contacts in the system.
    """
    if not contacts:
        print("📂 No contacts available.")
    else:
        print("\n📋 Contact List:")
        for name, phone in contacts.items():
            print(f"- {name}: {phone}")
        print()  # blank line for spacing


# -------------------------------------------
# Main Program Loop
# -------------------------------------------

print("📱 CONTACT MANAGEMENT SYSTEM")
print("Options:")
print("1. Add Contact")
print("2. Search Contact")
print("3. Display All Contacts")
print("4. Exit\n")

while True:
    choice = input("Enter choice (1–4): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)

    elif choice == "2":
        name = input("Enter name to search: ")
        search_contact(name)

    elif choice == "3":
        display_contacts()

    elif choice == "4":
        print("👋 Exiting Contact Management System. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please enter 1–4.")

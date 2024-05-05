import datetime

contacts = []  

def add_contact(name, phone, birthday):
    """Adds a new contact with name, phone number, and birthday (YYYY-MM-DD)."""
    contact = {
        "name": name,
        "phone": phone,
        "birthday": birthday  
    }
    contacts.append(contact)
    print(f"Contact '{name}' added successfully!")

def remove_contact(name):
    """Removes a contact by name."""
    for i, contact in enumerate(contacts):
        if contact["name"] == name:
            del contacts[i]
            print(f"Contact '{name}' removed.")
            return  # Contact found and removed

    print(f"Contact '{name}' not found.")

def display_contacts():
    """Displays all contacts in the list."""
    if contacts:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Birthday: {contact['birthday']}")
    else:
        print("Your contact list is empty.")
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts.append(Contact(name, phone, email))

def view_contacts(contacts):
    for contact in contacts:
        print(contact)

def save_contacts(contacts, filename):
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(f"{contact.name},{contact.phone},{contact.email}\n")

def load_contacts(filename):
    contacts = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, phone, email = line.strip().split(',')
                contacts.append(Contact(name, phone, email))
    except FileNotFoundError:
        print("No previous contacts found.")
    return contacts

contacts = load_contacts("contacts.txt")
while True:
    print("1. Add contact")
    print("2. View contacts")
    print("3. Save and exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        save_contacts(contacts, "contacts.txt")
        break
    else:
        print("Invalid choice. Please try again.")
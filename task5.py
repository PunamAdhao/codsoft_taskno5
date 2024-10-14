"""Contact Information: Store name, phone number, email, and address for each contact.
 Add Contact: Allow users to add new contacts with their details.
 View Contact List: Display a list of all saved contacts with names and phone numbers.
 Search Contact: Implement a search function to find contacts by name or phone number.
 Update Contact: Enable users to update contact details.
 Delete Contact: Provide an option to delete a contact.
 User Interface: Design a user-friendly interface for easy interaction"""

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name}: {self.phone}, {self.email}, {self.address}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print(f"Contact '{name}' added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("Contact List:")
        for contact in self.contacts:
            print(contact)

    def search_contact(self, query):
        found_contacts = [c for c in self.contacts if query.lower() in c.name.lower() or query in c.phone]
        if found_contacts:
            print("Search Results:")
            for contact in found_contacts:
                print(contact)
        else:
            print("No contacts found.")

    def update_contact(self, name, phone=None, email=None, address=None):
        for contact in self.contacts:
            if contact.name == name:
                if phone:
                    contact.phone = phone
                if email:
                    contact.email = email
                if address:
                    contact.address = address
                print(f"Contact '{name}' updated.")
                return
        print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted.")
                return
        print(f"Contact '{name}' not found.")


def main():
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone, email, address)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            manager.search_contact(query)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            manager.update_contact(name, phone if phone else None, email if email else None, address if address else None)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

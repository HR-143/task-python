class Contact:
    def _init_(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def _str_(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactManager:
    def _init_(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, query):
        found_contacts = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]
        if not found_contacts:
            print(f"No contacts found with the query: {query}")
        else:
            for contact in found_contacts:
                print(contact)

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Updating contact {name}. Leave field blank to keep current value.")
                new_name = input("Enter new name: ").strip() or contact.name
                new_phone = input("Enter new phone number: ").strip() or contact.phone
                new_email = input("Enter new email: ").strip() or contact.email
                new_address = input("Enter new address: ").strip() or contact.address

                contact.name = new_name
                contact.phone = new_phone
                contact.email = new_email
                contact.address = new_address
                print(f"Contact {name} updated successfully.")
                return
        print(f"Contact {name} not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully.")
                return
        print(f"Contact {name} not found.")

def menu():
    manager = ContactManager()
    
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
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
            manager.update_contact(name)
        
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)
        
        elif choice == '6':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Call the menu function directly without using the main check
menu()
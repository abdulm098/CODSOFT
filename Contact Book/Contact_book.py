contacts = []

def display_menu():  
    print("Contact Book Menu")
    print("1. Add a contact")
    print("2. Search for a contact")
    print("3. Update a contact")
    print("4. Delete a contact")
    print("5. Display all contacts")
    print("6. Exit")

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address=input("Enter the contact's address: ")
    contact = {"Name": name, "Phoneno": phone, "Email": email,"Address":address} 
    contacts.append(contact)
    print("Contact added successfully!")

def search_contact():
    search_term = input("Enter the name or phoneno or email or address  of the contact to search: ")
    found_contacts = [] 
    for contact in contacts:
        if search_term.lower() in contact["Name"].lower() or search_term.lower() in contact["Phoneno"].lower() or search_term.lower() in contact["Email"] or search_term.lower() in contact["Address"]:
            found_contacts.append(contact)  

    if found_contacts:  
        print("Matching contacts found:")
        for contact in found_contacts:  
            print("Name:", contact["Name"])
            print("Phone:", contact["Phoneno"])
            print("Email:", contact["Email"])
            print("Address:", contact["Address"])
            print("-------------------")
    else:
        print("No matching contacts found.")

def update_contact():
    
    name = input("Enter the name of the contact to update: ") 
    found_contact = None 
    for contact in contacts: 
        if contact["Name"].lower() == name.lower():
            found_contact = contact  
            break

    if found_contact: 
        print("Contact found. Enter new details:")
        found_contact["Name"] = input("Enter the new name: ")
        found_contact["Phoneno"] = input("Enter the new phone number: ")
        found_contact["Email"] = input("Enter the new email: ")
        found_contact["Address"] = input("Enter the  new address")
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
  
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:  
        if contact["Name"].lower() == name.lower():  
            contacts.remove(contact)   
            print("Contact deleted successfully!")
            break
    else:
        print("Contact not found.")    

def display_all_contacts():
   
    if contacts:
        print("All Contacts:")
        for contact in contacts:
            print("Name:", contact["Name"])
            print("Phoneno:", contact["Phoneno"])
            print("Email:", contact["Email"])
            print("Address:", contact["Address"])
            print("-------------------") 
    else:
        print("No contacts found.")

while True:
   
    display_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        display_all_contacts()
    elif choice == "6":
        print("Exiting the program...")
        break  
    else:
        print("Invalid choice. Please enter a valid option (1-6).")        

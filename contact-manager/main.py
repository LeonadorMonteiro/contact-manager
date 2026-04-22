import json

def load_contacs():
    try:
        with open("contacts.json", "r") as f:
            usuarios = json.load(f)
            return usuarios
    except FileNotFoundError:
        return []

usuarios = load_contacs()

def save_contacts(usuarios):
    try:
        with open("contacts.json", "w") as f:
            json.dump(usuarios, f)
    except FileNotFoundError:
        return []

def information(usuarios):
    name = input("Name: ")
    phone = int(input("Phone: "))
    email = input("Email: ")
    contacto = {
        "name": name,
        "phone": phone,
        "email": email
    }
    usuarios.append(contacto)
    print("\n"+ "-" * 20)
    print(f"Name: {name}")
    print(f"Phone: {phone}")
    print(f"Email: {email}")
    save_contacts(usuarios)

def show_menu():
    print("\n=== CONTACT LIST ===")
    print("1 - Add contact")
    print("2 - View all contacts")
    print("3 - Search contact")
    print("4 - Delete contact")
    print("5 - Exit")
    opcion = int(input("Choose one of the options by entering the number: "))
    return opcion

def view_contacts(usuarios):
    for i, contacto in enumerate(usuarios, start=1):
        print(f"\n--- Contact {i} ---")
        print(f"Name: {contacto['name']}")
        print(f"Phone: {contacto['phone']}")
        print(f"Email: {contacto['email']}")

def search_contacts(usuarios):
    search = input("Enter the name of the person you want to search for: ")
    for contacto in usuarios:
        if contacto["name"].lower() == search.lower():
            print("---- Contact found ----")
            print(f"Name: {contacto['name']}")
            print(f"Phone: {contacto['phone']}")
            print(f"Email: {contacto['email']}")
            break
    else:
        print("Contact not found")
def delete_contac(usuarios):
    delete = input("Enter the name of the person you want to delete: ")
    for contacto in usuarios:
        if  contacto["name"].lower() == delete.lower():
            print("---- Delete contact ----")
            usuarios.remove(contacto)
            print("The user has been deleted")
            save_contacts(usuarios)
            break
    else:
        print("Contact not found")
while True:
    opcion = show_menu()
    
    if opcion == 1:
        information(usuarios)
    elif opcion == 2:
        view_contacts(usuarios)
    elif opcion == 3:
        search_contacts(usuarios)
    elif opcion == 4:
        delete_contac(usuarios)
    elif opcion == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.")
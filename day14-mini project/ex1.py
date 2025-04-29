def get_menuchoice():
    print()
    print("My Address Book")
    print("*****************")
    print("1. search for a contacts")
    print("2. add a contact")
    print("3. update a contact")
    print("4. delete a contacts")
    print("5. quit the program")

    choice= int(input("Enter your choice: "))

    while choice < 1 or choice > 5:
        choice = int(input("Please enter valid choice(1-5): "))

    return choice
def search(contacts):
    name = input("Enter the name of contact to search: ")
    print(contacts.get(name,"not found"))

def add(contacts):
    name = input("Enter the name :")
    phone = input("Enter the phone number : ")
    if name  not in contacts:
        contacts[name] = phone
    else:
        print("Contact already exists")

def update(contacts):
    name=input("Enter the name for update: ")
    if name in contacts:
        phone = input("Enter the new phone number to update: ")
        contacts[name] = phone
    else:
        print("That contact does not exist")

def delete(contacts):
    name= input("Enter the name to delete(remove): ")
    if name in contacts:
        del contacts[name]
    else:
        print("Thet name does not exist")
        
def main():
    contacts= {}
    choice=0
    while choice != 5:
        choice = get_menuchoice()
        if choice == 1:
            search(contacts)
        elif choice == 2:
            add(contacts)
        elif choice == 3:
            update(contacts)
        elif choice == 4:
            delete (contacts)
main()
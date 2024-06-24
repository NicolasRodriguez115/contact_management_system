def import_contacts(contacts):
    import os
    os.system("cls")
    with open("contacts.txt", "r") as file:
        for line in file:
            number, name, email = line.split(';')
            contacts[number] = {f"Name:": {name}, "Email:": {email}}
            
    input("You've succesfully imported contacts.txt to the program! To continue press 'enter'\n ")

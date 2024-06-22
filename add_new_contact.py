def new_contact(contacts):
    import os
    os.system("cls")
    phone_number = input("Enter your contact phone number:\n")
    name = input("Enter the contact name:\n").capitalize()
    email = input("Enter the contact email addres:\n")
    contacts[phone_number] = {"Name:": name, "Email:": email}
    input("You've succesfully created a new contact! press 'enter' to exit\n ")
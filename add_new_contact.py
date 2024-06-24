def new_contact(contacts):
    import re
    import os
    os.system("cls")
    phone_number = input("Enter your contact phone number using the following pattern: xxx-xxx-xxxx\n")
    phone_number_pattern = re.compile("^\d{3}-\d{3}-\d{4}$")
    name_pattern = re.compile("(^[A-Z][a-z]+) ([A-Z][a-z]*)?\s?([A-Z][a-z]+)")
    email_patern = re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    while True:
        if re.match(phone_number_pattern, phone_number):
            name = input("Enter the contact name and last name:\n").title()
        else:
            input("You've entered a number that doesn't match the format. You'll return to the main manu after pressing 'enter'.\n ")
            return
        if re.match(name_pattern, name):
            email = input("Enter the contact email addres:\n")
        else:
            input("You've not entered a valid name. You'll return to the main manu after pressing 'enter'.\n ")
            return
        if re.match(email_patern, email):
            contacts[phone_number] = {"Name:": name, "Email:": email}
            input("You've succesfully created a new contact! press 'enter' to exit\n ")
            return
        else:
            input("You've not entered a valid email addres. You'll return to the main manu after pressing 'enter'.\n ")
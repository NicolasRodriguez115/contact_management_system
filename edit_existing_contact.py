def edit_contact(contact):
    import os
    os.system("cls")
    for id, info in contact.items():
        print(f"Phone number: {id}")
        for description, value in info.items():
            print(f"{description} {value}")
    phone_searched = input("Enter the phone number that you wanna search:\n")
    phone_selected = contact.get(phone_searched, False)
    if phone_selected:
        while True:
            print(f"""
1. Name: {phone_selected.get("Name:", "")}
2. Email: {phone_selected.get("Email:", "")}
3. Quit
""")
            option_selected = input("Select option that you want to edit:\n")
            if option_selected == "1":
                phone_selected["Name:"] = input("Enter the new name: ").capitalize()
                contact[phone_searched] = phone_selected
                os.system("cls")
                print(f"The new name is {phone_selected["Name:"]}.")
            elif option_selected == "2":
                phone_selected["Email:"] = input("Enter the new email: ")
                contact[phone_searched] = phone_selected
                os.system("cls")
                print(f"The new email is {phone_selected["Email:"]}.")
            elif option_selected == "3":
                return
            else:
                print("You've entered a wrong input. Please try again after pressing 'enter.'\n ")
    else:
        print("You didn't enter a valid phone number. Please try again after pressing 'enter.\n ")




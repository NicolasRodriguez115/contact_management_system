def delete_contact(contact):
    import os
    os.system("cls")
    for id, info in contact.items():
        print(f"Phone number: {id}")
        for description, value in info.items():
            print(f"{description} {value}")
    phone_searched = input("Enter the phone number of the contact you want to delete:\n")
    phone_selected = contact.get(phone_searched, False)
    while True:
        if phone_selected:
            phone_selected = contact.pop(phone_searched)
            input(f"You've succesfully deleted {phone_selected["Name:"]}. To go back to the main menu press 'enter'\n ")
            return
        elif phone_searched == False:
            input("You've not entered a valid phone number. Please try again after pressing 'enter'.\n")
            
        
    


    
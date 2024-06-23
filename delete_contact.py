def delete_contact(contacts):
    import os
    os.system("cls")
    for id, info in contacts.items():
        print(f"Phone number: {id}")
        for description, value in info.items():
            print(f"-{description} {value}")
    phone_searched = input("Enter the phone number of the contact you want to delete:\n")
    phone_selected = contacts.get(phone_searched, False)
    while True:
        if phone_selected:
            phone_selected = contacts.pop(phone_searched)
            input(f"You've succesfully deleted {phone_selected["Name:"]}. To go back to the main menu press 'enter'\n ")
            return
        elif phone_selected == False:
            input("You've not entered a valid phone number. Please try again after pressing 'enter'.\n")
            
        
    


    
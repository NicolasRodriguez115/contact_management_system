def contact_search(contacts):
    import os
    os.system("cls")
    phone_searched = input("Enter the phone number of the contact you're looking for to see their information. If you whish to return to the main menu type 'exit'\n").lower()
    phone_selected = contacts.get(phone_searched, False)
    while True:
        if phone_selected:
               for id, info in contacts.items():
                    print(f"Phone number: {id}\n")
                    for description, value in info.items():
                         print(f"-{description} {value}")
                    input("To go back press 'enter'.\n")
                    return
        elif phone_searched == "exit":
             return
        elif phone_selected == False:
            input("You've not entered a valid phone number. Please try again after pressing 'enter'.\n")
            
        

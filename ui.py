def data_storage_menu():
    from add_new_contact import new_contact
    from edit_existing_contact import edit_contact
    from delete_contact import delete_contact
    from search_for_contact import contact_search
    from display_contacts import display_contacts
    from export_contacts import export_contacts
    from import_contacts import import_contacts
    from main import contact_list
    import os
    while True:
        os.system("cls")
        user_input = input(
"""
Welcome to the contact management system!
Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import contacts from a text file
8. Quit 
""")
        if user_input == "1":
            new_contact(contact_list)
        elif user_input == "2":
            edit_contact(contact_list)
        elif user_input == "3":
            delete_contact(contact_list)
        elif user_input == "4":
            contact_search(contact_list)
        elif user_input == "5":
            display_contacts(contact_list)
        elif user_input == "6":
            export_contacts(contact_list)
        elif user_input == "7":
            import_contacts(contact_list)
        elif user_input == "8":
            break
        else:
            input("You've not entered a valid option. Please try again after pressing 'enter'\n ")    


def export_contacts(contacts):
    import os
    os.system("cls")
    with open("contact_list.txt", "w") as file:
       for id, info in contacts.items():
        name = info.get("Name:", "")
        email = info.get("Email:", "") 
        file.write(f"{id},{name},{email}\n")
    input(f"The list of contacts was succesfully exported to contact_list.txt! Press 'enter' to continue,\n ")
    return       

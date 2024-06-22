def display_contacts(contact):
   import os
   os.system("cls")
   for id, info in contact.items():
       print(f"Phone number: {id}")
       for description, value in info.items():
           print(f"{description} {value}")

   input("Press 'enter' to exit\n ")



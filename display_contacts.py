def display_contacts(contacts):
   import os
   os.system("cls")
   for id, info in contacts.items():
       print(f"Phone number: {id}")
       for description, value in info.items():
           print(f"-{description} {value}")

   input("Press 'enter' to exit\n ")



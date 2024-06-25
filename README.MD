# Contact List Application

The **Contact List Application** is a command-line program that allows users to manage a list of contacts. It provides various functionalities for adding, editing, deleting, searching, and displaying contact information.

## Usage

1.  **Adding a New Contact**:
    
    -   To add a new contact, select option 1 from the menu.
    -   Enter the contact’s details (such as name, phone number, email, etc.).
    -   The contact will be added to the  `contact_list`.
2.  **Editing an Existing Contact**:
    
    -   To update a contact’s information, choose option 2.
    -   Modify any field (e.g., phone number, email) for an existing contact.
3.  **Deleting a Contact**:
    
    -   If you want to remove a contact, select option 3.
    -   Enter the name of the contact to delete.
4.  **Searching for a Contact**:
    
    -   Use option 4 to search for a specific contact.
    -   Enter the name or other relevant details to find the contact.
5.  **Displaying All Contacts**:
    
    -   Option 5 displays the entire list of contacts stored in the  `contact_list`.
6.  **Exporting Contacts**:
    
    -   Choose option 6 to export contacts to a text file.
    -   The exported file will contain contact details.
7.  **Importing Contacts**:
    
    -   Option 7 allows you to import contacts from a text file.
    -   Provide the path to the file containing contact information.
8.  **Quitting the Application**:
    
    -   To exit the program, select option 8.

## Code Overview

### `contact_list`  Dictionary

-   The  `contact_list`  is a dictionary that stores contact information.
-   Each contact is represented as a key-value pair, where the key is the contact’s name, and the value is a dictionary containing various details (e.g., phone number, email).

### Main Menu Loop

-   The program runs in a loop, displaying the menu options.
-   Based on user input, it calls different functions (e.g.,  `new_contact`,  `edit_contact`) to perform specific tasks.

# Contact List Application: Adding a New Contact

The  `new_contact`  function in the Contact List Application allows users to add a new contact to their list. It validates user input for phone numbers, names, and email addresses before adding the contact to the  `contacts`  dictionary.

## Function Overview

### `new_contact(contacts)`

-   **Purpose**: Adds a new contact to the contact list.
-   **Parameters**:
    -   `contacts`: A dictionary representing the contact list. Each contact is stored as a key-value pair, where the key is the phone number, and the value is a dictionary containing contact details (name and email).
-   **Steps**:
    1.  Prompt the user to enter a phone number in the format  `xxx-xxx-xxxx`.
    2.  Validate the phone number using a regular expression pattern.
    3.  If the phone number is valid, prompt the user to enter the contact’s name (first name and last name).
    4.  Validate the name using another regular expression pattern.
    5.  If the name is valid, prompt the user to enter the contact’s email address.
    6.  Validate the email address using a third regular expression pattern.
    7.  If the email address is valid, add the contact to the  `contacts`  dictionary.
    8.  Display a success message and return to the main menu.
    9.  If any input is invalid, display an appropriate error message and return to the main menu.

## Regular Expression Patterns

1.  **Phone Number Pattern**:
    
    -   Format:  `xxx-xxx-xxxx`  (where  `x`  represents a digit).
    -   Example:  `123-456-7890`
2.  **Name Pattern**:
    
    -   Format: First name followed by an optional middle name and last name.
    -   Example:  `John Doe`  or  `Jane A. Smith`
3.  **Email Address Pattern**:
    
    -   Format: Valid email address (e.g.,  `user@example.com`

# Contact List Application: Editing a Contact

The  `edit_contact`  function in the Contact List Application allows users to modify existing contact information. Users can update the contact’s name or email address. The function validates user input and ensures that the changes are reflected in the contact list.

## Function Overview

### `edit_contact(contacts)`

-   **Purpose**: Allows users to edit an existing contact.
-   **Parameters**:
    -   `contacts`: A dictionary representing the contact list.
-   **Steps**:
    1.  Display the list of existing contacts along with their details (phone number, name, and email).
    2.  Prompt the user to enter the phone number of the contact they want to edit.
    3.  Retrieve the selected contact from the  `contacts`  dictionary.
    4.  Display a menu with the following options:
        -   Edit the contact’s name
        -   Edit the contact’s email
        -   Quit (return to the main menu)
    5.  Based on the user’s choice, update the contact’s information.
    6.  Display a success message and return to the main menu.

# Contact List Application: Deleting a Contact

The  `delete_contact`  function in the Contact List Application allows users to remove an existing contact from their list. Users can search for a contact by phone number and delete it if found. The function ensures that the contact is removed from the  `contacts`  dictionary.

## Function Overview

### `delete_contact(contacts)`

-   **Purpose**: Deletes an existing contact from the contact list.
-   **Parameters**:
    -   `contacts`: A dictionary representing the contact list.
-   **Steps**:
    1.  Display the list of existing contacts along with their details (phone number, name, and email).
    2.  Prompt the user to enter the phone number of the contact they want to delete.
    3.  Retrieve the selected contact from the  `contacts`  dictionary.
    4.  If the contact exists, remove it from the dictionary using the  `pop`  method.
    5.  Display a success message and return to the main menu.
    6.  If the entered phone number is invalid, display an appropriate error message and allow the user to try again.

# Contact List Application: Searching for a Contact

The  `contact_search`  function in the Contact List Application allows users to search for a specific contact by entering their phone number. If the contact exists, the function displays their information (name and email). Users can return to the main menu or continue searching for other contacts.

## Function Overview

### `contact_search(contacts)`

-   **Purpose**: Searches for a contact by phone number.
-   **Parameters**:
    -   `contacts`: A dictionary representing the contact list.
-   **Steps**:
    1.  Prompt the user to enter the phone number of the contact they’re looking for.
    2.  Convert the input to lowercase for case-insensitive searching.
    3.  Retrieve the selected contact from the  `contacts`  dictionary.
    4.  If the contact exists, display their details (phone number, name, and email).
    5.  Allow the user to return to the main menu or continue searching.
    6.  If the entered phone number is invalid, display an appropriate error message.

# Displaying Contacts

The  `display_contacts`  function retrieves and displays the contact information stored in the  `contacts`  dictionary. Each contact includes the following details:

-   **Phone number**
-   **Name**
-   **Email address**

## How to Use

1.  Ensure you have Python installed on your system.
2.  Save the provided code snippet to a file (e.g.,  `contact_list_app.py`).
3.  Open a terminal or command prompt.
4.  Navigate to the directory where the file is saved.
5.  Run the program using the command:  `python contact_list_app.py`.

## Example Output
```
Phone number: 123-456-7890
- Name: John Doe
- Email: john.doe@example.com

Phone number: 987-654-3210
- Name: Jane Smith
- Email: jane.smith@example.com
```
Press ‘enter’ to exit the display.

# Exporting Contacts

The  `export_contacts`  function saves the contact information from the  `contacts`  dictionary to a text file. Each line in the file represents a contact and includes the following details:

-   **Phone number**
-   **Name**
-   **Email address**

## How to Use

1.  Ensure you have Python installed on your system.
2.  Save the provided code snippet to a file (e.g.,  `contact_list_app.py`).
3.  Open a terminal or command prompt.
4.  Navigate to the directory where the file is saved.
5.  Run the program using the command:  `python contact_list_app.py`.

## Example Output (contact_list.txt)
```
123-456-7890,John Doe,john.doe@example.com
987-654-3210,Jane Smith,jane.smith@example.com
```
The exported file (`contact_list.txt`) will contain all the contacts in this format.

Press ‘enter’ to continue.

# Importing Contacts

The  `import_contacts`  function reads data from the  `contacts.txt`  file and updates the contact list stored in the  `contacts`  dictionary. Each line in the file represents a contact and follows this format:
```
Phone number;Name;Email
```
-   **Phone number**: The contact’s phone number (e.g.,  `123-456-7890`).
-   **Name**: The contact’s full name (e.g.,  `John Doe`).
-   **Email**: The contact’s email address (e.g.,  `john.doe@example.com`).

## Example  `contacts.txt`  Content

```
123-456-7890;John Doe;john.doe@example.com
987-654-3210;Jane Smith;jane.smith@example.com
```
The imported contacts will be added to the existing contact list.

Press ‘enter’ to continue.

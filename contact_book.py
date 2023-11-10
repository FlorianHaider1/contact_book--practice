# Create a program to manage a contact book.
# Each contact can have a name, phone number, email, and address.
# Practice Skills:
# Use a dictionary to store contacts (with names as keys).
# Use lists and tuples to store contact details.
# Practice adding, removing, and editing contacts, and searching for a specific contact.
# Implement string methods for formatting and validating input (like email format validation).
#
# To add: 
# Remove Contacts
# Add titles to prettytable
# Exception handling: Name already exists, to not overwrite. Emailadress is valid (@). Name = str, Phone = int
# Editing existing entries
# Export and import function to e.g. .csv  --- Which format is best for importing/exporting for databases?
# 


from prettytable import PrettyTable

# dictionary for all entries
contacts = {}

# data for entries
names = [("Mario"), ("Luigi"), ("Peach"), ("Toad"), ("Bowser"), ("Link"), ("Zelda")]
phone = [13579, 246810, 12345, 34567, 56789, 97542, 86420]
email = ["mario@home.com", "luigi@luigi.com", "preach@gmail.com", "toad@shell.com", "bowser@aol.com", "link@hyrule.com", "zelda@hyrule.com"]


# creation of a list of entry tuples: 
# first 'manual' tuple creation to practice 
# overview_manual = []
# for i in range(len(names)):
#     overview_manual.append((names[i], phone[i], email[i]))
# second tuple creation via function

overview = list[:]


# Generation of tupled list
def create_database():
    overview = list(zip(names, phone, email))
    return overview


#import entries into dictionary with keys = names and values = tuples.
def import_to_dictionary():
    for nam, phon, mail in create_database():
        contacts[nam] = nam, phon, mail
    return contacts


# table to print the entries 
def display_contacts():
    table = PrettyTable()
    for values in contacts.values():
        table.add_row(values)
    print(table)



# console to navigate contact book
def open_contact_book():
    start = str(input("Welcome to your contact book. \n Press (C) to view your contacts. \n Press (A) to add new contact:"))
    if start.upper() == "C":
        display_contacts()     
    if start.upper() == "A":
        new_contact()

# adding new contacts
def new_contact():
    new_name = str(input("Please enter new contact name: "))
    names.append(new_name)
    new_phone = str(input("Please enter new contact phone number: "))
    phone.append(new_phone)
    new_email = str(input("Please enter new contact email address: "))
    email.append(new_email)
    print("Your contact book has been succesfully updated.\n")
    import_to_dictionary()
    display_contacts()

#  set up all in the right order
def start_up():
    import_to_dictionary()
    open_contact_book()

start_up()

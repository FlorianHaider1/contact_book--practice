# Create a program to manage a contact book.
# Each contact can have a name, phone number, email, and address.
# Practice Skills:
# Use a dictionary to store contacts (with names as keys).
# Use lists and tuples to store contact details.
# Practice adding, removing, and editing contacts, and searching for a specific contact.
# Implement string methods for formatting and validating input (like email format validation).

import PrettyTable

contacts = {}

#data for entries
names = [("Mario"), ("Luigi"), ("Peach"), ("Toad"), ("Bowser"), ("Link"), ("Zelda")]
phone = [13579, 246810, 12345, 34567, 56789, 97542, 86420]
email = ["mario@home.com", "luigi@luigi.com", "preach@gmail.com", "toad@shell.com", "bowser@aol.com", "link@hyrule.com", "zelda@hyrule.com"]


# creation of a list of entry tuples: 
# first 'manual' tuple creation to practice 
overview_manual = []
for i in range(len(names)):
    overview_manual.append((names[i], phone[i], email[i]))
# second tuple creation via function
overview_function = list(zip(names, phone, email))


#import entries into dictionary with keys = names and values = tuples.
for nam, phon, mail in overview_function:
    contacts[nam] = nam, phon, mail

pprint.pprint(contacts)




# coding=utf-8
__author__ = "Laura Bolčina"

# Contact class
class Contact(object):
    """ Contact class for saving contacts. """
    def __init__(self, first_name, last_name, email, phone, address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    def full_name(self):
        """ Method for returning full name of a contact. """
        full = self.first_name + " " + self.last_name
        return full

print "Welcome to the contacts app!"

add = True
contacts = []

# app asks the user if he wants to add a contact (in a loop); if not, the program prints contacts and stops
while add:
    adding = raw_input("Do you want to add a new contact? (y/n) ")
    if adding in "yY":
        first_name = raw_input("First name: ")
        last_name = raw_input("Last name: ")
        address = raw_input("Address: ")
        phone = raw_input("Phone number: ")
        email = raw_input("Email address: ")
        new_contact = Contact(first_name, last_name, email, phone, address) # creates a new object "new_contact" with entered data
        contacts.append(new_contact) # adds a contact to "contacts" list
        print "Contact successfully added."
    elif adding in "nN":
        if contacts != []:
            print "Contacts:"
            for person in contacts: # prints full name of each one of contacts in the list
                print person.full_name()
            print "Goodbye!"
            add = False
        else:
            print "Goodbye!"
            add = False
    else:
        print "Enter 'y' to add a new contact or 'n' to quit."
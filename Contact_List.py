# Ben Sklar
# Contact List Program.
# Demonstrates using dictionaries and lists within them.
# Allows for Phone Numbers and E-Mails.
# Includes all Extensions.
# Random names, phone numbers, and e-mails used.

# Contact List, is a dictionary with a list.
contacts = {"Ben Sklar": ["555-555-5555", "bsklar@gmail.com"],
        "Sarah Dumont": ["534-245-6456", "sdumont@gmail.com"],
        "Alex Bri": ["315-293-4213", "abri@gmail.com"],
        "Brian Bro" : ["892-125-6502", "bbro@gmail.com"],
        "James Dro" : ["435-234-1634", "jdro@gamil.com"],
        "Hermione Rodri" : ["315-921-1234", "hrodri@gmail.com"]}

# Prints existing contacts at the beginning of the program.
print("Current Contacts: ")

# Sorts the contacts alphabetically.
for name in sorted(contacts):
    print(name)

# While loop as long as you don't quit.
choice = None
while choice != "0":

    print(
    """
    Contact List:

    0 - Quit.
    1 - Look up a Contact.
    2 - Add a Contact.
    3 - Delete a Contact.
    4 - Edit a Contact.
    5 - Print Alphabetical Contact List.
    """
    )

    choice = input("Choice: ")
    print()

    # To Quit/Exit.
    if choice == "0":
        print("Your Contact List has been terminated.")

    # Lookup a contact.   
    elif choice == "1":
        name = input("What Contact do you want to lookup?: ")
        if name in contacts:
            contact_list = contacts[name]
            print(name + "'s Phone Number:", contact_list[0])
            print(name + "'s E-mail:", contact_list[1])
        else:
            print("\nSorry, I don't know", name + "'s phone number.")

    # Add a contact.     
    elif choice == "2":
        name = input("What's the name of the contact you want to add to the Contact List?: ")
        if name not in contacts:
            contacts[name] = ["number", "e-mail"]
            number = input("\nWhat's his/her 10-digit phone number?: ")
            contacts[name][0] = number
            email = input("\nWhat's his/her e-mail?: ")
            contacts[name][1] = email
            print("\n", name, "has been added.")
        else:
            print("\nThat name already exists! Try a different name.")

    # Delete a contact.
    elif choice == "3":
        name = input("What contact do you want to delete? ")
        if name in contacts:
            del contacts[name]
            print("\n", name, "has been deleted successfully.")
        else:
            print("\nI can't do that!", name, "doesn't exist in the Contact List.")

    # Edit a contact.
    elif choice == "4":
        name = input("What contact name do you want to edit?: ")
        if name in contacts:
            contacts[name] = ["number", "e-mail"]
            number = input("\nWhat's his/her new phone number?: ")
            contacts[name][0] = number
            email = input("\nWhat's his/her new e-mail?: ")
            contacts[name][1] = email
            print("\n", name, "has been edited.")
        else:
            print("\nThat contact name doesn't exist!")


    # Prints alphabetical contact names. Prints the phone numbers, and e-mails as well.
    elif choice == "5":
        print("NAME: \t\t\tPHONE NUMBER: \t\tE-MAIL:")
        for name in sorted(contacts):
            contact_list = contacts[name]
            print(name, "\t\t", contact_list[0], "\t\t", contact_list[1])

    # Incase the user gives an invalid option.
    else:
        print("\nSorry, but", choice, "isn't a valid option.")

input("\n\nPress the enter key to exit.")

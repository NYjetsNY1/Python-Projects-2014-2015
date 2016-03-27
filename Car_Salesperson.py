# Ben Sklar
# Program Function-> Buying a vehicle, interacting, and finding price totals.
# Uses prompts, input statements, print statements, variables, /n, /t, etc.

#Prompt to continue program.
input("Hello and Welcome to Sklar\'s Cars! Please Press Enter to Continue...")

#Prompt user to input name and address.
firstname=input("What is your first name? ")
lastname=input("What is your last name? ")
address=input("What is your address? ")

#Shows firstname, lastname, address, then prompts the user to continue.
print("Hello",firstname,lastname,)
print("Your address is",address,)
input("If this is correct, please press enter...")

#Prompts for car, price, and spits it back out.
carname=input("\nWhat car do you want to purchase today? ")
baseprice=float(input("What is the base price of your vehicle? $"))
print("Your vehicle's base price is $", baseprice,)

#Tax is 14%.
taxcost= baseprice* .14
print("\n\tBase Cost = \t\t$", baseprice,)
print("\tTax(14%) = \t\t$", taxcost,)

#Licensing Fee is 5%.
licensefee= baseprice * .05
print("\tLicense Fee(5%) = \t$", licensefee,)

#Dealer Preparation Fee is 250 dollars.
print("\tDealer Fee = \t\t$ 250.0")
dealerprep= 250

#Registration Fee is 1000 dollars.
print("\tRegistration Fee = \t$ 1000.0")
registrationcost= 1000

#Miscellaneous Price Fee is 500 dollars.
print("\tMiscellaneous Fee =\t$ 500.0")
misc= 500

#Calculates total by adding all the variables, and then spits it out.
total = baseprice + taxcost + licensefee + dealerprep + registrationcost + misc
print("\t------------------------------------")
print("\tTotal =", " \t\t$", total,)

#Ends the program with a prompt to press enter.
print("\n\n\nYour Final Price For The", carname, "is $", total,)
print("\nThank you for visiting Sklar\'s Cars today. \n\nIf you would like to purchase the", carname,  "please see Ben Sklar.")
input("\n\nPress the enter key to exit.")

'''
Intent: Begin to provide options for the form of one person to be addressed.

Postconditions: The following are on the console (excluding the numbering):
1.
Greetings from a beginning Python programmer.
2.
Do you want to be addressed as ...
.......................................======>Jane Margaret Doe?
.......................................======>Jane Doe?
.......................................======>Mr./Ms. Jane Margaret Doe?
.......................................======>Dear Jane?
or
.......................................======>Doe, Jane Margaret?
3.
After a blank line, the same output, but applied to Archibald Montague Abercrombie
4.
After a blank line, the same output, but applied to Cleopatra Anastasia Montgomery
'''

greeting = "Greetings from a beginning Python programmer."  # Storing the basic greeting into a string
addressed = "Do you want to be addressed as ..."  # Storing the address variable into a string

print("\n" + greeting)  # Printing the basic greeting, along with a linespace to begin
print(addressed)  # Printing the address variable

arrows = ".......................................======>"  # Storing the intro arrows into a string
firstName = "Jane"  # Storing first name for later use
middleName = "Margaret"  # Storing middle name for later use
lastName = "Doe"  # Storing last name for later use

# The below functions print out the arrows and names in the specified formats, per the postcondition
# We have added the format function for each print statement to format the text easier
print(arrows + "{0} {1} {2}?".format(firstName, middleName, lastName))
print(arrows + "{0} {2}?".format(firstName, middleName, lastName))
print(arrows + "Mr./Ms. {0} {1} {2}?".format(firstName, middleName, lastName))
print(arrows + "Dear {0}?".format(firstName, middleName, lastName))
print("or")
print(arrows + "{2}, {0} {1}?".format(firstName, middleName, lastName))
print()

# Next we are storing the new names in the strings we previously used so we can copy the first format print lines and
# reuse the formats
firstName = "Archibald"  # Storing next first name for later use
middleName = "Montague"  # Storing next middle name for later use
lastName = "Abercrombie"  # Storing next last name for later use

# The below functions print out the arrows and names in the specified formats, per the postcondition
# We have added the format function for each print statement to format the text easier
print(arrows + "{0} {1} {2}?".format(firstName, middleName, lastName))
print(arrows + "{0} {2}?".format(firstName, middleName, lastName))
print(arrows + "Mr./Ms. {0} {1} {2}?".format(firstName, middleName, lastName))
print(arrows + "Dear {0}?".format(firstName, middleName, lastName))
print("or")
print(arrows + "{2}, {0} {1}?".format(firstName, middleName, lastName))
print()

# Next we are storing the new names in the strings we previously used so we can copy the first format print lines and
# reuse the formats
firstName = "Cleopatra"  # Storing final first name for later use
middleName = "Anastasia"  # Storing final middle name for later use
lastName = "Montgomery"  # Storing final last name for later use

# The below functions print out the arrows and names in the specified formats, per the postcondition
# We have added the format function for each print statement to format the text easier
print(arrows + "{0} {1} {2}?".format(firstName, middleName, lastName))
print(arrows + "{0} {2}?".format(firstName, middleName, lastName))
print(arrows + "Mr./Ms. {0} {1} {2}?".format(firstName, middleName, lastName))
print(arrows + "Dear {0}?".format(firstName, middleName, lastName))
print("or")
print(arrows + "{2}, {0} {1}?".format(firstName, middleName, lastName))
print()

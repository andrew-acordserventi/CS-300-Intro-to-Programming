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
'''

greeting = "Greetings from a beginning Python programmer." #Storing the basic greeting into a string
addressed = "Do you want to be addressed as ..." #Storing the address variable into a string

print("\n" + greeting) #Printing the basic greeting, along with a linespace to begin
print(addressed) #Printing the address variable

arrows = ".......................................======>" #Storing the intro arrows into a string
firstName = "Jane" #Storing first name for later use
middleName = "Margaret" #Storing middle name for later use
lastName = "Doe" #Storing last name for later use

#The below functions print out the arrows and names in the specified formats, per the postcondition
print(arrows + firstName + " " + middleName + " " + lastName + "?")
print(arrows + firstName + " " + lastName + "?")
print(arrows + "Mr./Ms. " + firstName + " " + middleName + " " + lastName + "?")
print(arrows + "Dear " + firstName + "?")
print("or")
print(arrows + lastName + ", " + firstName + " " + middleName + "?")
'''
Eliza300: Postconditions
1. (Welcome): A welcome message is on the console
2. (Complaint): A complaint was entered by the user in response to a prompt
3. (Duration): A duration in months was entered by user in response to a prompt
4. (Error check): EITHER the user entered an integer between 1 and 100 for duration after being given up to two chances
    OR the application quit after suggesting a re-run.
5. (Action Recommended): EITHER how_long exceeds 2 months, and the phrase
   “ … months is too much time to go without help! Let's schedule a few
   sessions" is on the console OR the following is on the console:
   "Come back in a couple of months if this persists".
'''
import sys # Imports sys to use the exit function

greeting = "Thank you for using Eliza300, a fun therapy program."  # Storing greeting as a string
print(greeting)  # Printing the greeting
complaint = input("Please state your emotional complaint then hit ENTER: \n")  # Getting input from the user with a
# prompt to store their complaint in the complaint string
print("I am sorry to hear you report \"" + complaint + "\"!")  # Printing the user's complaint back to them

duration = input("How many months have you been experiencing \"" + complaint + "\"? \n")# Asks user for input to
# store the duration of months of their complaint

# The below checks for numeric value for user input. If the user inputs numeric values, it changes to string to an int.
# If the user did not enter a number, it gives them a second chance. If they enter a number, it changes it to an int.
# If the user still does not change to an int, they get a re-run message and the program ends.
if duration.isnumeric():
    duration = int(duration)
else:
    duration = input("The number you entered is invalid. Please enter a valid number and try once more.\n")
    if duration.isnumeric():
        duration = int(duration)
    else:
        print("The number you entered is invalid. Please rerun the Eliza300 and try again.")
        sys.exit()

# The below checks for duration between 2 and 100. If the number of months is between 2 and 100, it schedules.
# If the number of months is above 100, it asks for more input and does another int check like the previous paragraph.
# If the number of months is within 2-100, then the scheduling line comes up.
# If the number of months is <= 2, then the program tells the user to come back again.
if duration > 2 and duration < 100:
    print(str(duration) + " months is too much time to go without help! Let's schedule a few sessions.")
elif duration > 100:
    duration = input("Please try one more time to enter duration in less than 100 months:\n")
    if duration.isnumeric():
        duration = int(duration)
    else:
        duration = input("The number you entered is invalid. Please enter a valid number and try once more.\n")
        if duration.isnumeric():
            duration = int(duration)
        else:
            print("The number you entered is invalid. Please rerun the Eliza300 and try again.")
            sys.exit()
    if duration > 100:
        print("The number you entered exceeds 100 months. Please rerun the Eliza300 and try again.")
        sys.exit()
    elif duration > 2 and duration < 100:
        print(str(duration) + " months is too much time to go without help! Let's schedule a few sessions.")
    else:
        print("Please come back if this problem persists for more than 2 months.")
else:
    print("Please come back if this problem persists for more than 2 months.")
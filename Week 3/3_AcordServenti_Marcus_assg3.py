# Eliza300
# Intent: A list of helpful actions that a troubled person could take. Build 2

possible_actions = ['taking up yoga', 'sleeping eight hours a night', 'relaxing',
                    'not working on weekends', 'spending two hours a day with friends']

'''
Precondition: possible_actions is the list defined above

Postconditions:

1. (Welcome): A welcome message is on the console

2. (user_complaint): user_complaint is the user's response to
"Please describe your emotional complaint--in one punctuation-free line: "

3. (how_long): how_long is the user's string response to
"How many months (between 1 and 99) have you experienced ...?"

4. (Month validity): EITHER how_long has the requested form
OR this terminated AND "Sorry, illegal input. Eliza is quitting; run Eliza again."
is on the console

5. (Advice): EITHER how_long >= 3
OR "Please return in * months" is on the console where * is 3 - how_long

6. (actions_not_taken): actions_not_taken consists of the actions (elements) in
possible_actions that the user answered 'n' to when questioned "Have you tried..."

7. (Summarized): Eliza300 recommended that the user take the actions in
actions_not_taken
'''

import sys

print("Thank you for using Eliza300, a fun therapy program.")

# Gets the complaint from the user.
user_complaint = input("Please describe your emotional complaint in one punctuation-free line:\n")

# Gets the number of months from the user
how_long = input("How many months (between 1 and 99) have you experienced \"" + user_complaint + "?\"\n")

# Error checking for a valid integer to store.
if how_long.isnumeric():
    how_long = int(how_long)
else:  # Exits the system if an invalid number or other variable is input
    print("Sorry, illegal input. Eliza is quitting; run Eliza again.")
    sys.exit()

# Checking to ensure the input is between 1 or 99; if it's not, the system exits
if how_long < 1 or how_long > 99:
    print("Sorry, illegal input. Eliza is quitting; run Eliza again.")
    sys.exit()

print(str(how_long) + " months is significant. I'm sorry to hear that.")

# Creating the try_list array to store ideas for the user to try and the prompt for later use
try_list = []
prompt = "Have you tried..."

# if loop to check duration.
if how_long < 3:  # Duration too low - print simple return statement and exit program
    print("Please return if this issue persists for more than 3 months.")
    sys.exit()
elif how_long >= 3:  # Duration higher than 3
    for x in possible_actions:  # For loop prints all possible actions (Stored from prompt above)
        try_response = input(prompt + x + "? Please answer y or n:\n")  # Asks the user what they have tried
        if try_response == "y":  # If the user has tried the idea, skip the elif statement and goto next try
            continue
        elif try_response == "n":  # If the user has not tried, then append the try_list
            try_list.append(x)

# If the user has already tried everything, the try_list is empty, so exit the program
if len(try_list) == 0:
    print("You have tried all recommendations.")
    sys.exit()

print("After careful analysis, here is Eliza300's advice:")

for x in try_list:  # Prints the list of things the user has not tried
    print(x.capitalize() + ".")
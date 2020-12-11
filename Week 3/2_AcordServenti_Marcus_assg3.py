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
OR this terminated AND "Sorry, illegal input. Eliza is quitting; please run Eliza again."
is on the console

5. (Advice):
EITHER how_long < 3 AND "Please return in * months" is on the console where *
is 3-how_long
OR how_long >= 3 AND The phrases in possible_action are on separate lines
on the console, each preceded by "Try ".
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
else: # Exits the system if an invalid number is input
    print("Sorry, illegal input. Eliza is quitting; run Eliza again.")
    sys.exit()

# Checking to ensure the input is between 1 or 99; if it's not, the system exits
if how_long < 1 or how_long > 99:
    print("Sorry, illegal input. Eliza is quitting; run Eliza again.")
    sys.exit()

print(str(how_long) + " months is significant. I'm sorry to hear that.")

# if loop to check duration.
if how_long < 3: # Duration too low - print simple return statement.
    print("Please return if this issue persists for more than 3 months.")
elif how_long >= 3: # Duration higher than 3
    for x in possible_actions: # For loop prints all possible actions (Stored from prompt above)
        print("Try " + x)
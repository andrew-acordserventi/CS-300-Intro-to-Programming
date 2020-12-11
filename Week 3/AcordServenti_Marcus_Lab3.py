# Eliza300
# Intent: A list of helpful actions that a troubled person could take. Build 1

possible_actions = ['taking up yoga.', 'sleeping eight hours a night.', 'relaxing.',
        'not working on weekends.', 'spending two hours a day with friends.']

'''
Precondition: possible_actions is the list defined above

Postconditions:
1. (Welcome): A welcome message is on the console
2. (user_complaint): user_complaint is the user's response to a prompt for the
user's complaint
3. (how_long): how_long is the user's string response to "How many months have
you experienced ...?" AND Eliza300 sympathized, mentioning the duration
4. (Advice):
EITHER how_long < 3 AND "Please return in * months" is on the console where *
is 3-how_long
OR how_long >= 3 AND The phrases in possible_action are on separate lines
on the console, each preceded by "Try ". 
'''

import sys

print("Thank you for using Eliza300, a fun therapy program.")

# Gets the complaint from the user.
user_complaint = input("Please describe your emotional complain in one punctuation-free line:\n")

# Gets the number of months from the user
how_long = input("How many months have you experienced \"" + user_complaint + "?\"\n")

# Error checking for a valid integer to store.
if how_long.isnumeric():
    how_long = int(how_long)
else: # Second chance to input a number in case of mistyping
    how_long = input("The number you entered is invalid. Please enter a valid number and try once more.\n")
    if how_long.isnumeric():
        how_long = int(how_long)
    else:
        print("The number you entered is invalid. Please rerun the Eliza300 and try again.")
        sys.exit()

print(str(how_long) + " months is significant. I'm sorry to hear that.")

# if loop to check duration.
if how_long < 3: # Duration too low - print simple return statement.
    print("Please return if this issue persists for more than 3 months.")
elif how_long >= 3: # Duration higher than 3
    for x in possible_actions: # For loop prints all possible actions (Stored from prompt above)
        print("Try " + x)
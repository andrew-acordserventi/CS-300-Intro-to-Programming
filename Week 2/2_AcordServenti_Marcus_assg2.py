'''
Eliza300: Postconditions
1. (Welcome): A welcome message is on the console
2. (Complaint): A complaint was entered by the user in response to a prompt
3. (Duration): A duration was entered by user in response to a prompt
4. (Action Recommended): EITHER how long exceeds 2 months, and the phrase
   “ … months is too much time to go without help! Let's schedule a few sessions"
   is on the console
   OR the following is on the console:
   "Come back in a couple of months if this persists".
'''

greeting = "Thank you for using Eliza300, a fun therapy program."  # Storing greeting as a string
print(greeting)  # Printing the greeting
complaint = input("Please state your emotional complaint then hit ENTER: \n")  # Getting input from the user with a
# prompt to store their complaint in the complaint string
print("I am sorry to hear you report \"" + complaint + "\"!")  # Printing the user's complaint back to them

duration = input("How many months have you been experiencing \"" + complaint + "\"? \n") # Asks user for input to
# store the duration of months of their complaint
duration = int(duration) # Stores the duration entered as an integer instead of string

if duration < 2: # Checks to see if duration is longer than 2 months
    print("Please come back if this problem persists for more than 2 months.") # Prints message telling user to come
    # back since it duration is 2 months or less
else:
    print(str(duration) + " months is too much time to go without help! Let's schedule a few sessions.") # If
    # duration is more than 2 months, program tells user to schedule some sessions

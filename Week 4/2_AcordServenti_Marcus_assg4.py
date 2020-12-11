# A list of types of emotional complaints and corresponding key words for each
complaint_type = ['Depression', 'Human Relations', 'Substance Abuse']
key_words = [['depress', 'sad', 'down'],
             ['conflict', 'argument', 'mistreat', 'quarrel'],
             ['drug', 'alcohol', 'drink', 'cocaine', 'opioid', 'heroin']]

def get_complaint_type(user_complaint): # Function to check user complain against key words
    mySet = set() # Creates a blank set
    index = 0 # Sets the index to 0
    for types in key_words: # Checks the key word list
        for type in types: # Checks the individual element of the sublist
            if type in user_complaint.lower(): # If the user input matches an element
                mySet.add(index) # Add the sublist index to the empty set
                break # Don't check further if it matches once
        index = index + 1 # Moves to the next index
    return mySet # Returns the set of sublist entries

'''
    Precondition:
    1. a_user_complaint is a string
    2. complaint_type is a list of strings
    3. key_words is a list of lists of strings
    3. complaint_type and key_words are the same length

    Returns: observed_complaint_type, which consists of the indices in
    complaint_type that correspond to key_words elements partly in a_user_complaint.

    Example: if the user enters “I’ve been saddened by world conflicts”,
    the function returns the set consisting of 0 and 1 because “I’ve been saddened …”
    contains “sad” and “conflict”.
'''

'''
Postconditions
1 (Welcome): A welcome message is on the console  
2 (user_complaint): user_complaint is the user's response in reply to "Please state your complaint:"
3 (observed_complaint_types): observed_complaint_types = get_complaint_type(user_complaint)
4 (Indices displayed): observed_complaint_types is on the monitor
'''

# (Welcome): Postcondition 1
print("Thank you for using Eliza300, a fun therapy program.")

# (user_complaint): Postcondition 2
print("Please state your complaint:")
user_complaint = input()

# (observed_complaint_type): Postcondition 3
observed_complaint_type = get_complaint_type(user_complaint) # Calls the get_complaint_type function and stores return

# (Advice displayed): Postcondition 4
if len(observed_complaint_type) > 0: # Checks if the function has anything in it or not
    print(observed_complaint_type) # Prints the indices




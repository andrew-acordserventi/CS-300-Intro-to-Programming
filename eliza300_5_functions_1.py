from Build3 import eliza300_5_runtime_data

# A list of types of emotional complaints and corresponding key words for each (REMOVED)
'''
complaint_type = ['Depression', 'Human Relations', 'Substance Abuse']
key_words = [['depress', 'sad', 'down'],
             ['conflict', 'argument', 'mistreat', 'quarrel'],
             ['drug', 'alcohol', 'drink', 'cocaine', 'opioid', 'heroin']]
'''
# Gets complaint types and key words from the runtime_data file
complaint_type = eliza300_5_runtime_data.complaint_types
key_words = eliza300_5_runtime_data.key_words

# List of advice per type of complaint
advice_per_type = [
    ['Get out more.', 'Take up a hobby that you love.'],
    ["Don't expect too much of people.", "Don't take offence easily."],
    ['Get counseling.', "Don't delay action on counseling."]]

def get_complaint_type(user_complaint): # Function to check user complaint against key words
    mySet = set() # Creates a blank set
    index = 0 # Sets the index to 0
    for types in key_words: # Checks the key word list
        for subtype in types: # Checks the individual element of the sublist
            if subtype in user_complaint.lower(): # If the user input matches an element
                mySet.add(index) # Add the sublist index to the empty set
                break # Don't check further if it matches once
        index = index + 1 # Moves to the next index
    return mySet # Returns the set of sublist entries

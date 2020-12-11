'''
   Intent: Get complaint_types and key_words from local ElizaData.txt

   Precondition =========

   ElizaData.txt is a local file consisting of paragraphs of the form

   On first line: 'Key Words for '<phrase describing a complaint category>
   On second line: <words, separated by blanks, that may occur within a
   description of the corresponding category>

   Example of ElizaData.txt:

   Key Words for Depression
   depress sad

   Key Words for Human Relations
   conflict argument mistreat

   Postconditions =========

   (1) complaint_types = list of the phrases in ElizaData.txt describing all
   complaint categories
   {2) key_words = list of lists of words in ElizaData.txt that may occur
   within phrases that describe the corresponding complaint category

   '''
from Build3 import eliza300_5_functions_1
from Build3 import eliza300_5_runtime_data

print("Thank you for using Eliza300, a fun therapy program.")

print("Please state your complaint:")
user_complaint = input()

observed_complaint_type = eliza300_5_functions_1.get_complaint_type(user_complaint)  # Calls the get_complaint_type
# function and stores return

if len(observed_complaint_type) > 0:  # Checks if the function has anything in it or not
    for x in range(len(eliza300_5_runtime_data.key_words)):  # Begins a loop against the length of the key_words
        if x in observed_complaint_type:  # If the current iteration exists in the user complaint, the next line
            # triggers
            for element in eliza300_5_functions_1.advice_per_type[x]:  # If the user complaint contains a key word,
                # then store the index of the individual advice_per_type as an element to loop
                # through the entire advice list
                print(element)  # Print the individual index of the advice_per_type

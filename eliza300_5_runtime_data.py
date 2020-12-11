global complaint_types # Creating global instance of complaint types
global key_words # Creating global instance of key words

complaint_types = [] # Creating a list
key_words = [] # Creating a list

def read_complaint_data(): # This function reads the text file
    complaint_database = "ElizaData.txt" # Storing the text file in a variable
    current_database = open(complaint_database, "rt") # Opens the text file
    line_read = current_database.readline().rstrip() # Reads the current line
    while line_read != "": # The quotes indicate the end of the text file; while the end of the file is not reached,
        # this keeps looping
        current_index = line_read.find("for") # Finds the keyword for, then stores it as an index
        complaints = line_read[current_index+4:] # Skips 4 spaces beyond for and stores it as a complaint
        complaint_types.append(complaints) # Appends the complaint type list with the current complaint
        line_read = current_database.readline().rstrip() # Reads the next line
        subwords = line_read.split(" ") # Looks for spaces in the next line and splits the words by a space; stores as
        # a subword
        key_words.append(subwords) # Adds the subword to the key_word list
        line_read = current_database.readline().rstrip() # Reads the next line
        if len(line_read) < 1: # If the line is a blank, this will skip the blank line
            line_read = current_database.readline().rstrip()
    current_database.close() # Closes the text file stored

read_complaint_data()  # need to execute this here

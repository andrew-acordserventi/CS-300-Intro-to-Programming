'''
Postconditions
1 (Welcome): A welcome message is on the console
2 (Complaint): A complaint was entered by the user in response to a prompt
AND Eliza has responded "I am sorry to hear you report <the complaint entered by the user>"
'''

greeting = "Thank you for using Eliza300, a fun therapy program."  # Storing greeting as a string
print(greeting)  # Printing the greeting
complaint = input("Please state your emotional complaint then hit ENTER: \n")  # Getting input from the user with a
# prompt to store their complaint in the complaint string
print("I am sorry to hear you report \"" + complaint + "\"!")  # Printing the user's complaint back to them

# myString = "This is a string"
# secondString = 'Random'
# print(str(myString) + " is of data type " + str(type(myString)))
# print(secondString)

# INPUT
# In coding, information that a user enters is known as input. You will use a built-in function named input() to get information from the user. 
# The input() function will pause the code until a user enters a string and presses ENTER. Return to the Python script:

name = input("What's your name? ")
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))
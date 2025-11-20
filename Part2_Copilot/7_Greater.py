# Please write a program which asks for two integer numbers. 
# The program should then print out whichever is greater.
# If the numbers are equal, the program should print a different message.

# Some examples of expected behaviour:

# Sample output
# Please type in the first number: 5
# Please type in another number: 3
# The greater number was: 5

# Sample output
# Please type in the first number: 5
# Please type in another number: 8
# The greater number was: 8

# Sample output
# Please type in the first number: 5
# Please type in another number: 5
# The numbers are equal!

# Write your code here:
number1=int(input(" Please type in the first integer number "))
number2=int(input(" Please type in the second integer number"))
if number1 > number2 : print("The greater number was: " + str(number1))
elif number2 > number1 : print("The greater number was: " + str(number2))
else : print("The numbers are equal!") 

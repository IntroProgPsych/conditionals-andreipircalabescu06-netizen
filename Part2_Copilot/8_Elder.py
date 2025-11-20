# Please write a program which asks for the names and ages of two persons.
# The program should then print out the name of the elder.

# Some examples of expected behaviour:

# Sample output
# Person 1:
# Name: Alan
# Age: 26
# Person 2:
# Name: Ada
# Age: 27
# The elder is Ada

# Sample output
# Person 1:
# Name: Bill
# Age: 1
# Person 2:
# Name: Jean
# Age: 1
# Bill and Jean are the same age

# Write your code here:
age1=int(input(" Please type in the age of Person 1 "))
name1=input(" Please type in the name of Person 1 ")
age2=int(input(" Please type in the age of Person 2 "))
name2=input(" Please type in the name of Person 2 ")
if age1 > age2 : print("The elder is " + name1)
elif age2 > age1 : print("The elder is " + name2)
else : print(name1 + " and " + name2 + " are the same age")

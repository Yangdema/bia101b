#objective:
#create a program that takes in user input
#and determines if the number is positive or negative 
#input: "your number is positive " or "your number is negative"

#if else 
#print()
#input()


#brake down the problem
#1 take in user input 
#2 check the type of the input 
#if the type is string, how do you convert it into int
#check if the number is positive or negative or zero
#need to use if else statement


#number=int(input("10:"))
#if number> 0:
    #print("the number is positive")

userInput = input('please type any number ')
userInputType = type(userInput)
print('the type of user input is:', userInputType)
userInputNumber = float(userInput) 
print("the type of userInputNumber is:",type( userInputNumber))

if userInputNumber > 0:
    print('the number is positive')
if userInputNumber < 0:
    print('the number is negative')
if userInputNumber ==0:
    print('the number is zero')

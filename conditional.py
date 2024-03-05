
# objective: a calculater application made using 
#variables and if statements
#steps 
#1. get input from the user 
#2. do calculation based on user input 
#3. give output to the user
#print('above user input')
#userinput =''
print ('* for multiplication')
print('+for addition') 
print('- for subtraction')
print('/ for division')

whatUserTyped = input()

print('user typed:', whatUserTyped)
print('user input-type', type(whatUserTyped))
print('------')
if whatUserTyped == "+":
    print('doing addition')
    if 'a' == 'b':
        print('a is not b')
    if 'b' == 'b':
        print('b is b')

print('doing more addition')

if whatUserTyped == "-":
    print('doing subtraction')
    print('doing more subtraction')



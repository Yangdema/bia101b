#Dechen - D3ch3n
#Hello - H3llo
#Tshewang - 75h3wa4n9
#loops#A -4
#o - 0
#e - 3
#l - 1
#s - 5
#g - 9
#b - 6
#t - 7

#testName = "Tshewang"


#arrayFruits = ["apple", "orange ", "banana", "grapes"]

#for fruit in arrayFruits:
    #if fruit == "grapes":
        #print("grapes found")result = ""
result = ""
testName = "Tshewang"
for char in testName:
    if char == "A":
        result += "4"
    elif char == "o":
        result += "0"
    elif char == "e":
        result += "3"
    elif char == "l":
        result += "1"
    elif char == "s":
        result += "5"
    elif char == "g":
        result += "9"
    elif char == "b":
        result += "6"
    elif char == "t":
        result += "7"
    elif char == "z":
        result += "2"
    else:
        result = result + char

print(result)



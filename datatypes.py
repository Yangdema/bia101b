#creation of arrays
array1 = [1,2,3,"thimphu",2.5]
#retrieving element
element1 = array1[0]
element2 = array1[4]
lastElement = array1[-5]
print(lastElement)

#modifying elements
array1[0] = 10

#print(element2)
#print(array1)
#getting number of elements is an array
no_of_elements = len(array1)
print(no_of_elements)
#slicing
elements = array1[0:3]
print(elements)

arr1 = [1,10]
arr2 = ['thimphu', 'wangdue']

number_to_check =2
result = number_to_check in arr1 
print('result is',result)
arr3= arr1 + arr2
print(arr3)
arrVariable = [1,3,2]
arrVariable.append(4)
print(arrVariable)

#insert at specific index
arrVariable,insert(1,10)

arrVariable.sort()
print(arrVariable)

stackVar = []
#adding to stack
stackVar.append(4)
stackVar.append(2)
stackVar.append(9)
stackVar.append(1)
print('after appending', stackVar)
element = stackVar.pop()
print('after popping', stackVar)
print('after ')




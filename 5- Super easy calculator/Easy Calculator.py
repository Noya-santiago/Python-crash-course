""" We're gonna make a basic calculator!! """

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1+num2 #If you dont specify what are those variables python will understand they as strings... so the result would be the number following the another

print(result)

result = int(num1)+int(num2) #The result (if its not a comma number, will be given) (if its a comma number we have to make them floats)

print(result)
""" When programming, often we want to obtain one value from one specific function. What we do is we use the return statement.
the return statement will give the function itself, the value of that return line of code. For example. if the funtion name is 
Pedro_function. And the last name of the function is return 3. DOES NOT matter what happened before, pedro_function's value is 3. """

def cube(num):
    return num*num*num
    #print("This won't be printed :(")

result = cube(5)
print(result)
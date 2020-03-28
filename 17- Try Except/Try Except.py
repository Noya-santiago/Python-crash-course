""" We can grab errors and store them into a variable with this command, also works as error avoiding xD """


try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError as err:
    print("Wrong value")
    print(err)
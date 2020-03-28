print("There once was a man named John")
print("he was 35 years old.")
print("He really liked the name John, ")
print("but didnt like being 35")

""" Basically there are several types of variables in python. Booleans, Strings, Floats, etc.
We can call any variables as the name we want to. Just by typping Variable_name = variable_value
the strings variables will be represented with "", booleans with "False or True" and the floats
with just numbers. As we can see, i can write exactly the same as before but using variables """

character_name = "John"
character_age = 35 

print("There once was a man named "+ character_name +", ")
print("he was" + str(character_age) + "years old.") #In this scenario we have to change the variable to string because python cant interpet a integer next to a string
print("He really liked the name "+ character_name +",")
print("but didnt like being "+ str(character_age) +".")

# We can also add another Boolean variable
is_male = False

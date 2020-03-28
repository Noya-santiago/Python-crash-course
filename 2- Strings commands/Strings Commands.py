""" In the next code we will see different type of commands that we can use to modify strings in the fly
for example; we will use string_variable.upper() when we want to convert de string into uppercase symbols
we will use .lower() when we want to transform it to lowercase .title() for tittles and so on"""

phrase = "I really LIKE Banenas"

print(phrase + " Normal phrase")
print(phrase.lower() +" Lowercase")
print(phrase.upper() +" Uppercase")
print(phrase.title() +" Title shit")

# We can also use some functions that returns a value if something is happening, i.e. 

print(phrase.isupper()) #the function ("is upper") is asking if all the string variable is in uppercase, if the answer is yes the commmand
# will print a "True" (We can also store that value into another variable) """

is_the_phrase_upper = phrase.isupper() 
print(is_the_phrase_upper)

#Another useful command is "Len" command. We will be using that command far later, but in that case it tells you the LENgth of the phrase

print(len(phrase)) 
print(phrase[3]) #By using brackets we can tell the phrase to say one specific character
print(phrase.index("L")) #also the exact opposite
print(phrase.replace("Banenas", "apples")) #Its obvious 
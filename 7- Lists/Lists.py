""" That's actually pretty serious stuff.
The lists basically stores some values inside a large variable
we can call this variable however we want and store all kind of 
variables. They are called lists, matrixes, or arrays. For making one
we have to type a braket and store information separated with commas """

friends = ["Kevin", "Karen", "Jim"] #This array will store those 3 names in it. We can see it by printing it
print(friends)
""" We can also make functions with all of those arrays. Typping array_name[element_number] will select the specific number of the array
do you remember when I said that len command will be useful later? well. For arrays, its incredibly powerful, it tells you the number
of element of an array """

print(friends[2]) #Will print the third item of the array (We are counting 0) so will be "Jim"
print(len(friends)) #Will print the length of the array
print(friends[-2]) #If we type negative numbers will count from backwards
print(friends[1:]) #A colon is like a parenthesis in maths. Will print element 0, and 1, not 2

""" We can also change all of those variables """

friends.append("Oscar") #Will add to an array
friends.append("Toby")
friends [1] = "Miky"

print(friends[2:4])

#Some useful functions, you'll be able to understand them just by looking the prints

lucky_numbers = [4,8,4,3,15,16,23]
friends.extend(lucky_numbers)
print(friends)
friends.insert(3, "element three has been changed")
print(friends)
friends.remove("element three has been changed")
print(friends)
friends.clear()
print(friends)

"""We can also use array_name.pop() to erase one random number of the array, array_name.count(element name) for counting how many times
a specific value repeats himself, array_name.sort() for sorting .reverse() to reverse it and so on"""

"""Tuples.
A tuple is a kind of list that cannot be changed. Its written with ()"""

my_tupple = (1,2,3,4,5)
#we can also make a array of tupples
my_tupple_array = [(2,4),(3,5),(8)]
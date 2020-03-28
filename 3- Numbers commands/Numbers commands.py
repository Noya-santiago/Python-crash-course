""" Python sees numbers as weird things... For examples, for python a 4 is a integer, but, a 4.0 is a float. You can also
use some mathematical functions that you will be looking in case you need them """


print(3+4) #Python is gonna print 7. As an integer
print(3.0+4.0) #Python is gonna print 7.0000. As a float
print(3.5+4.5) #Again float

#Now some functions

print(pow(4, 6))
print(abs(-90))
print(max(4,5,6,7,2))
print(round(4.5))

#there is also a library called "Math". If we import the library we can use another ecuations (We will be talking about import libs later)

from math import *

print(floor(3.6))
print(ceil(3.4))
print(sqrt(25))
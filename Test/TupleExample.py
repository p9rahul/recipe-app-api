
"""
It is like a list but immutable -> Hash DS -> Faster access 
Tuple items are ordered(order will not change), unchangeable, and allow duplicate values.

Tuple Items - Data Types ->String, int and boolean data types

============
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
============

"""
mytuple1 = ("apple", "banana", "cherry")
mytuple2 = ("apple", "banana", "cherry", "apple", "cherry")  #duplicate
mytuple3 = ("apple",) #Create Tuple With One Item
mytuple4 = ("abc", 34, True, 40, "male") # A tuple with strings, integers and boolean
# print(mytuple)
# print(type(mytuple)) #class

#Access yuple
print(mytuple1[1]) #You can access tuple items by referring to the index number, inside square brackets
print(mytuple1[-1]) #last item of the tuple
print(mytuple2[2:5]) #Range of Indexes
print(mytuple2[:4]) # from start to 4 items
print(mytuple2[2:]) # from 2nd index to last
print(mytuple2[-4:-1]) # Range of Negative Indexes -> from last 4th index to last 1st index

#
if "apple" in mytuple2:
    print("yes")

#Update/change tuple values -> Convert tuple to list and add , then convert back
x = ("apple", "banana", "cherry") # tuple
y = list(x) # convert to list
y[1] = "kiwi" 
x = tuple(y) # convert list to tuple
print(x)

# Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",'Mango')
thistuple += y #thistuple = thistuple +y

print(thistuple)

# Remove Items -> immutable so change it to list then remove and convert back to tuple 

#Delete - del
deltuple = ("apple", "banana", "cherry")
del deltuple
# print(deltuple) #this will raise an error because the tuple no longer exists , it is deleted on before line

#loop Tuple
lTuple = ("apple", "banana", "cherry")
for x in lTuple:
  print(x)
# Loop Through the Index Numbers
lTuple = ("apple", "banana", "cherry")
for i in range(len(lTuple)):
  print(lTuple[i])

# Using a While Loop
wtuple = ("apple", "banana", "cherry")
i = 0
while i < len(wtuple):
  print(wtuple[i])
  i = i + 1

ctuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)  #Count no of accourance
x = ctuple.count(5)
print(x)
x = ctuple.index(8) # index position
print(x)

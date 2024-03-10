#list mutuable -> change anything add, remove
nums =[10,24,56,78,76]
print (nums.pop(2)) #The pop() method removes the specified index.
print (nums.remove(76)) #The remove() method removes the specified item. and return None
del nums[1] #The del keyword also removes the specified index
nums.clear() #The clear() method Clear the list content
print (nums)

# # Loop Through a List
for x in nums:
    print (x)

# # Loop Through the Index Numbers
for i in range(len(nums)):
    print ("Loop Through the Index Numbers", nums[i])

# #While loop
i=0
while i<len(nums):
    print(nums[i])
    i = i+1

# Looping Using List Comprehension -> offers the shortest syntax for looping through lists
[print(x) for x in nums]

#https://www.w3schools.com/python/python_lists_methods.asp
"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""

# extend()	Add the elements of a list, to the end of the current list
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#Append -> Another way to join two lists, one by one
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# Join Two Lists using the + operator
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
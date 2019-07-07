# working with lists
# we can put any data type in the list
# list is indexed with 0
friends = ["Diksha","Rajni","Manjunath"]
print(friends)  # prints actual list
print(friends[2])

# back of the list start from -1
print(friends[-2])  # access elements from the back of the list

# splitting the list
print(friends[1:])  # start from index position 1 and all other elements

print(friends[1:2])  # access elements in the range 1 to 2, doesn't include the last element

# updating the list elements
friends[1] = "Ranjan"
print(friends)

# List functions
# List can store quite large number of values

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar","Toby"]

print(friends)

# extend function() add list to another list

friends.extend(lucky_numbers)
print(friends)
# adding item to the end of the list
friends.append("Creed")
print(friends)

friends.insert(1, "Kelly")
print(friends)

# remove the elements

friends.remove("Jim")
print(friends)

# pop function() removes the last element of the list
friends.pop()
print(friends)

# to check if element is there in the list
print(friends.index("Kevin"))
# print(friends.index("Mike"))  # gives an error as Mike is not in the list

print(friends.count("Jim")) # tells the count of particular element in the list

# sorting the list
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)


# copy() function creates a copy of list
friends2 = friends.copy()
print(friends2)

# remove all the elements of the list
friends.clear()
print(friends)


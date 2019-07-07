# while loop
# allows to execute a block of code multiple times

i = 1
while i <= 10:
    print(i)
    i = i + 1

print("Done with the Loop")

# For Loops
for letter in "Giraffe Academy":
    print(letter)

friends = ["jim", "Karen", "Kevin"]

for friend in friends:
    print(friend)

for index in range(10):  # range start from 0 to n-1 i.e. 0 to 9
    print(index)

for index in range(3, 10):
    print(index)

for friend_index in range(len(friends)):
    print(friends[friend_index])

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not First")


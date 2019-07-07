# working with strings
print("Giraffe academy")
# to add new line
print("Giraffe \nacademy")
# escape character
print("Giraffe \"Academy\"")
print("Giraffe\\Academy")

phrase = "Giraffe Academy"
print(phrase)

# concatenation (adding another string to current string)
print (phrase + " is cool")

# string functions
# lower case
print(phrase.lower())

# upper case
print(phrase.upper())

# check if upper or lower case
print(phrase.isupper())
print(phrase.islower())

# chaining of function calls
print(phrase.upper().isupper())

# length of string (using len() function())
print(len(phrase))

# getting individual character of string
print(phrase[0])  # gets the first character of string (indexing starts from 0)

print(phrase[3])  # accessing the fourth character of string (a)

# getting index of character in string
print(phrase.index('a'))  # gets the first occurrence of a characters

print(phrase.index("Academ"))

# character which doesn't exist returns an error
# print(phrase.index("Deep"))

# replace function
print(phrase.replace("Giraffe","Ace"))
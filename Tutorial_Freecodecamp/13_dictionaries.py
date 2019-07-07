# Dictionaries like the map in Java
# keys have to be unique
month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April"
}

print(month_conversions["Jan"])
print(month_conversions.get("Jan"))

print(month_conversions.get("Luv"))  # returns None if no default is put

print(month_conversions.get("Luv","Not a valid key"))
print(month_conversions.get("Luv",-1))


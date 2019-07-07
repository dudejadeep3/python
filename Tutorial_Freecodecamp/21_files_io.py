# reading file
# modes of files "r", "w", "a" (append)
employee_file = open("employee.txt","r")  # open employee.txt file in read mode
print(employee_file.readable())
print(employee_file.readline())
print(employee_file.readline())
print("=================")
employee_file.close()

employee_file = open("employee.txt","r")  # open employee.txt file in read mode
line_list =employee_file.readlines()
print(line_list[0])
employee_file.close()

employee_file = open("employee.txt","r")  # open employee.txt file in read mode
for employee in employee_file.readlines():
    print(employee)
employee_file.close()

# writing to file(appending)

employee_file = open("employee.txt","a")
employee_file.write("\nKelly - Customer Service")
employee_file.close()

# writing to file (override the entire file)
employee_file = open("employee1.txt","w")
employee_file.write("\nKelly - Customer Service")
employee_file.close()

# writing to file (override the entire file)
employee_file = open("index.html","w")
employee_file.write("<p> This is the html file</p>")
employee_file.close()
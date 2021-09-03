employee_file = open("Employees.txt", "r")
print(employee_file.readable())

#print(employee_file.read())
#print(employee_file.readline())
#print(employee_file.readlines())

for employee in employee_file.readlines():
    print(employee)

employee_file.close()

employee_file_write = open("Employees.txt", "a")
#employee_file_write.write("\nTim - stress test")
employee_file_write.writelines("Tim - stress test")
employee_file_write.close()

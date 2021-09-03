# example comment
print("Comments are fun")

'''
 hello this is for comment
'''

try:
    value = 10 / 0
    number = int(input("Enter the number : "))
    print(number)
except ZeroDivisionError as error:
    #print("Divide by zero" + error)
    print(error)
except ValueError:
    print("invalid input")


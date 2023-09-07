# get first number
first_number = input("Please enter the first number: ")
# get second number
second_number = input("Please enter the second number: ")
# get the operation
operation = input("Please enter the operation (ADD, SUB, DIV, MUL):")
# check which operation was selected
if operation == "ADD":
    # add the numbers
    result = int(first_number) + int(second_number)
elif operation == "SUB":
    # subtract the number
    result = int(first_number) - int(second_number)
elif operation == "DIV":
    # subtract the number
    result = int(first_number) / int(second_number)
elif operation == "MUL":
    # subtract the number
    result = int(first_number) * int(second_number)
#return the result to the user
print("The result is: ", str(result))
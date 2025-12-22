from parser import find_number

expression = input("Enter your expression (enter EXIT to exit): ")

while expression != "EXIT":
    print(find_number(expression))
    expression = input("Enter your expression (enter EXIT to exit): ")

print("thank you for using my calculator!")
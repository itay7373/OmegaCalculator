from parser import calc, preparing_expression

expression = input("Enter your expression (enter EXIT to exit): ")

while expression.upper() != "EXIT":
    try:
        print(f"\nthe answer is: {calc(expression)}\n---------------------------")
    except Exception as e:
        print(f'Error: {e}\n---------------------------\n')

    expression = input("Enter your expression (enter EXIT to exit): ")

print("thank you for using my calculator!")

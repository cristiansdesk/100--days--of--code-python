def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

math = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide
        }

def calculator():
    should_continue = True
    num1 = float(input("Please choose a number: "))
    while should_continue:
        for symbol in math:
            print(symbol)
        symbol = input("Please choose an operation symbol: ")
        num2 = float(input("Please choose a number: "))
        calculation_function = math[symbol]
        result = calculation_function(num1, num2)
        print(f"{num1} {symbol} {num2} = {result}")
        continue_cal = input("Would you like to continue or start a new calculation? Type 'y' to continue or 'n' to quit:").lower()
        if continue_cal == 'y':
            num1 = result
        else:
            should_continue = False
            print("\n" * 30)
            calculator()


calculator()

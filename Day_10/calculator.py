

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "*": multiply,
    "+": add,
    "-": sub,
    "/": divide
}

print("*" in operations)
def calculator():
    continuation = True
    first_num = float(input('What\'s your first number: '))
    for symbol in operations:
        print(symbol)
    while continuation:
        # if continuation == 'n':
        # if continuation == 'y':
        operation = input('Pick an operation: ')
        next_num = float(input('What\'s your next number?: '))
        result = 0
        if operation in operations:
            calculation_function = operations[operation]
            result = calculation_function(first_num, next_num)
            print(f"{first_num} {operation} {next_num} = {result}")
        else:
            print('Invalid operation')

        continue_calculation = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation: ")
        if continue_calculation == 'n':
            continuation = False
            calculator()
        if continue_calculation == 'y':
            first_num = result


calculator()
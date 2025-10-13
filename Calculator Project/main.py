import operator

import art
# Calculator Project
def add(n1, n2):
    return n1 + n2

# pause 1
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

# pause 2
operator_dict = {'+': add,
             '-': sub,
             '*': mul,
             '/': div,
             }

# # pause 3
# print(operator_dict['*'](4, 8))

# Functionality
def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What's the first number?: "))
    while should_accumulate:

        for symbol in operator_dict:
            print(symbol)
        operator = input("Pick an operator: ")
        num2 = float(input("What's the next number?: "))

        answer = operator_dict[operator](num1, num2)
        print(f"{num1} {operator} {num2} =  {answer}")

        choose = input(f"Type 'y' to continue calculating with {operator}, or type 'n' to start a new calculation: ").lower()
        if choose == 'y':
            num1 = answer

        else:
            should_accumulate = False
            print("\n" * 20)
            calculator() # recursion - re calling fnc inside same fnc

calculator() # calling calculator fnc



"""CLI application for a prefix-notation calculator."""
# TODO: handle errors

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


def calculate():
    while True:
        equation = input("Enter your equation > ")
        tokens = equation.split(' ')

        if tokens[0] == 'q':
            break

        if tokens[0] != 'q':
            tokens[1] = float(tokens[1])

        if len(tokens) == 3:
            tokens[2] = float(tokens[2])

        if tokens[0] == '+':
            result = add(tokens[1], tokens[2])
            print(result)

        if tokens[0] == '-':
            result = subtract(tokens[1], tokens[2])
            print(result)

        if tokens[0] == '*':
            result = multiply(tokens[1], tokens[2])
            print(result)

        if tokens[0] == '/':
            result = divide(tokens[1], tokens[2])
            print(result)

        if tokens[0] == 'square':
            result = square(tokens[1])
            print(result)

        if tokens[0] == 'cube':    
            result = cube(tokens[1])
            print(result)

        if tokens[0] == 'pow':
            result = power(tokens[1], tokens[2])
            print(result)

        if tokens[0] == 'mod':
            result = mod(tokens[1], tokens[2])
            print(result)

calculate()

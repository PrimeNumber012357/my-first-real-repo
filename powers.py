#program that asks for 2 numbers and raises the first number by the second number 

def x_to_y(x, y):
    return float(x)**float(y)
base_number = input("Enter a base number: ")
exponent = input("Enter an exponent: ")
print("You chose " + str(base_number) + " and raised it to a power of " + str(exponent) + " and the result is " + str(x_to_y(base_number, exponent)))


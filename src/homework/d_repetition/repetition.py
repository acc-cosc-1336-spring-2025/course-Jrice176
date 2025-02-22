#
def get_factorial(num):
    factorial = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
            print("The factorial of", num, "is", factorial)

def sum_odd_numbers(num):
    sum = 0
    value = 1
    while (value < (2*num)-1):
        if value % 2 == 1:
            sum += value
        value += 1
    return sum
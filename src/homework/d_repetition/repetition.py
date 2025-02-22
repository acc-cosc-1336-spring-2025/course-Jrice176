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

def sum_odd_numbers(maximum):
    odd_total = 0
    number = 1
    while (number <= maximum):
        if(number % 2 != 0):
            print("{0}".format(number))
            odd_total = odd_total + number
        number = number + 1

    print("The Sum of Odd Numbers from 1 to {0} = {1}".format(maximum, odd_total))
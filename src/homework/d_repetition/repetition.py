#
from math import factorial


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


def run_hw_menu():
    print('Homework 3 Menu')
    print('1 - factorial')
    print('2- sum odd numbers')
    print('3 - exit')
    user_option = '0'

    while(user_option != '3'):
        run_hw_menu()
        user_option = input("Enter a menu option(1,2,3): ")
        handle_menu(user_option)
def handle_menu(user_option):
    if (user_option == '1'):
        num = input('Enter a number: ')
        result = get_factorial(int(num))
        print ("factorial:", result)
    elif (user_option == '2'):
        maximum = input('Enter a number: ')
        result = sum_odd_numbers(int(maximum))
        print("sum of odd numbers:", result)
    elif (user_option == '3'):
        print("Do you want to continue?")
    else:
        print("Invalid number")


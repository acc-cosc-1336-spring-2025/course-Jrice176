import repetition

def main():
    
    #num = input("Enter a number: ")
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
            result = repetition.get_factorial(int(num))
            print ("factorial:", result)
        elif (user_option == '2'):
            maximum = input('Enter a number: ')
            result = repetition.sum_odd_numbers(int(maximum))
            print("sum of odd numbers:", result)
        elif (user_option == '3'):
            print("Do you want to continue?")
        else:
            print("Invalid number")
    
    
    
main()
import input_process_output

def main():
    num1 = input("Enter a number: ")
    num2 = input("Enter a number: ")

    result = input_process_output.add_numbers(int(num1),int(num2))
    print(result)

main()
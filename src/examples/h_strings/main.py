#main program
import strings
def main():
    password = ""
    while not strings.validate_password(password):
        password = input("Enter Password")
    print(password)
main()
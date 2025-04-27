from class_a import die
def main():
    my_die = die()
    for i in range(1):
        print(my_die.roll())
        print("Run program to roll again...")
main()
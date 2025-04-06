#
import dictionary
def main():
    def display_menu(option):
        print('1-Get p distance matrix')
        print('2 - Exit')
        option = input('Enter 1 or 2')
        if option == 1:
            lists = input('Enter a list(s)')
            result = dictionary.get_p_distance_matrix(lists)
            return result
    main()
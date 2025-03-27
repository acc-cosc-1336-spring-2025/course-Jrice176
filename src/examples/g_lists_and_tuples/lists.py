def test_config():
    return True

def list_as_function_parameter(list1):
    list1[0] = 100

def display_multiplication_table(list):
    for row_list in list:
        for item in row_list:
            print(str(item).rjust(3," "), end = " ")
        print(" ")
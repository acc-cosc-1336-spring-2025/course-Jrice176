#output comments variables input calculations output constants
def display_output():
    print('hello')

def test_config():
    return True

def use_int_type():
    num = 10
    print(num)
    num = num + 5
    print(num)
    num = "Python"
    print(num)

def use_float_type():
    num = 10.99
    print(num)   

def use_string_type():
    lang = Python # type: ignore
    print(lang)

    lang = 10
    print(lang)

    lang = 10.99
    print(lang)

def add_numbers(num1,num2):
    result = num1 + num2

    return result
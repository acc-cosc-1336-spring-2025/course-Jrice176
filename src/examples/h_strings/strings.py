from operator import index


def test_config():
    return True

def string_params(str1):
    print(str1)
    str1 = "C++"

def string_return_value(lang):
    lang = "C++"
    print(id(lang))
    return lang

def string_loop_w_while(str):
    index = 0
    length = len(str)
    while(index < length):
        print(str[index], index, length)
        index += 1
        if (index == 6):
            print("",index, length)

def string_loop_w_for_range(str):
    length = len(str)
    for index in range(0, length):
        print(str[index], index, length)
        if (index == 6):
            print("",index, length)

def string_loop_w_for(str):
    for ch in str:
        print(ch)
        ch = 'a'
    print(str)

def validate_password(password):
    correct_length = 7
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    if(len(password) >= 7):
        correct_length = True
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True

        if correct_length and has_uppercase and has_lowercase and has_digit:
            is_valid = True
        else:
            is_valid = False

        return is_valid
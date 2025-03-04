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

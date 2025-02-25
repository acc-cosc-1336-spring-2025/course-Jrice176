value = 100#global variable

def test_config():
    return True

def echo_variable(num):
    return num

def read_global_variable():
    print(value)

def write_global_variable():
    global value
    value = 50
    print(value)
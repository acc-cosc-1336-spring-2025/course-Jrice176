def test_config():
    return True

def use_a_while_loop(num):

    counter = 0

    while(counter < num):
        print(counter, counter < num,'Hello')
        counter = counter +1
        #statement that makes boolean expression false

def get_sum_of_squares(num):
    sum = 0
    while(num > 0):
        sum = sum + num * num
        num = num - 1 #will make num > 0 false

    return sum
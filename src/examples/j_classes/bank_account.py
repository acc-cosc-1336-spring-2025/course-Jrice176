class BankAccount():
    __balance = 0
    def __init__(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance;
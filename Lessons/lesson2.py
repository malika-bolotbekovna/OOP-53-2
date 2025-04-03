class BankAccount:
    def __init__(self, name, balance, password):
        self.name = name
        self._balance = balance
        self.__password = password

    def top_up_balance(self, amount):
        if amount > 0:
            self._balance += amount
            return "баланс пополнен"
        else:
            return "сумма должна быть положительной!"
        
    def reset_password(self):
        self.__password = 1234
        return 'reset password'


ardager = BankAccount('Ardager', 100, 123)
 
print(ardager._balance)
print(ardager._BankAccount__password)
print(ardager.reset_password())
print(dir(ardager))


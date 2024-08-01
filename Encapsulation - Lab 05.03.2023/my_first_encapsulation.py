class BankAccount:
    def __init__(self, username: str, iban: str, balance: int):
        self.username = username
        self.__iban = iban          # private -> __attr
        self._balance = balance    # protected -> _attr

    @property               # private attr GETTER (shows value)
    def iban(self):
        return self.__iban

    @iban.setter            # private attr SETTER (changes value)
    def iban(self, value):
        self.__iban = value

    def show_balance(self):
        return f"New IBAN is: {self._balance}"


person = BankAccount("John", "BG12345673", 20000)
print(person.username)
print(person.iban)
person.iban = "BG56019410"
print(person.iban)
print(person.show_balance())
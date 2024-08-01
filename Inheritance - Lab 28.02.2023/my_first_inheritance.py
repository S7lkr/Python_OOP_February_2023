class Person:
    def __init__(self, name, age, nation):
        self.name = name
        self.age = age
        self.nation = nation

    def __repr__(self):
        return f"Name: {self.name}, years: {self.age} from {self.nation}."

    def stats(self):
        return f"Person description."


class FootballPlayer(Person):
    def __init__(self, name, age, nation, t_shirt_num):
        super().__init__(name, age, nation)
        self.t_shirt_num = t_shirt_num

    def stats(self):
        super().stats()
        return f"This is a {self.__class__.__name__} with Number: {self.t_shirt_num}"


class Scientist(Person):
    def __init__(self, name, age, nation, iq):
        super().__init__(name, age, nation)
        self.iq = iq

    def stats(self):
        super().stats()
        return f"This is a {self.__class__.__name__} with iq: {self.iq}"


person1 = FootballPlayer("Messi", 28, "Argentina", "30")
person2 = Scientist("Donald", 45, "USA", "200")
print(person1)
print(person1.stats())
print(person2)
print(person2.stats())
import random


class Car:
    _year = (2000, 2020)

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.hybrid = False

    def hybrid_check(self):     # check if hybrid engine
        if self.year > 2018:
            self.hybrid = True
            return f"{self.model} is hybrid!"
        return f"{self.model} is not a hybrid!"

    def car_details(self):      # full car details
        return f"{self.model}, Year: {self.year}, Hybrid engine: {self.hybrid}"


oldest, newest = Car._year                      # Car._year[0], Car._year[1]

seat = Car("Leon", random.randint(oldest, newest))         # gets a RANDOM year for every car: from 2000 to 2020
toyota = Car("Corolla", random.randint(oldest, newest))

print(seat.hybrid_check())
print(seat.car_details())
print(toyota.hybrid_check())
print(toyota.car_details())
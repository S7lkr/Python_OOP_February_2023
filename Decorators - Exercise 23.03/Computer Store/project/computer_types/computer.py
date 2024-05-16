from abc import ABC, abstractmethod
from math import log, floor, ceil


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price: int = 0

    @property
    @abstractmethod
    def available_processors(self):
        pass

    @property
    @abstractmethod
    def max_ram(self):
        pass

    @staticmethod
    def power_of_two(ram: int):
        result = log(ram, 2)
        return floor(result) == ceil(result)

    @property
    @abstractmethod
    def pc_type(self):
        pass

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value) -> ValueError or None:
        if value.strip() == "":
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value) -> ValueError or None:
        if value.strip() == "":
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    def configure_computer(self, processor: str, ram: int) -> ValueError or str:
        if processor not in self.available_processors.keys():
            raise ValueError(f"{processor} is not compatible "
                             f"with {self.pc_type} {self.manufacturer} {self.model}!")
        if not self.power_of_two(ram) or ram > self.max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.pc_type} {self.manufacturer} {self.model}!")
        self.processor = processor
        self.ram = ram
        self.price = log(ram, 2) * 100 + self.available_processors[processor]
        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price:.0f}$."

    def __repr__(self) -> str:
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
from typing import List
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse: List[DesktopComputer, Laptop] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer == "Desktop Computer":
            computer = DesktopComputer(manufacturer, model)
        elif type_computer == "Laptop":
            computer = Laptop(manufacturer, model)
        else:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        self.warehouse.append(computer)
        configuration = computer.configure_computer(processor, ram)
        return configuration

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int) -> str or Exception:
        try:
            computer = next(filter(lambda pc: pc.processor == wanted_processor and
                       pc.ram >= wanted_ram and
                       pc.price <= client_budget, self.warehouse))
        except StopIteration:
            raise Exception("Sorry, we don't have a computer for you.")
        self.profits += client_budget - computer.price
        self.warehouse.remove(computer)
        return f"{computer} sold for {client_budget}$."
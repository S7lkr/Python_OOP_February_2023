from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, element: str):
        self.data.append(element)

    def pop(self):
        el = self.data.pop()
        return el

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) < 1

    def __str__(self):
        return "[" + ", ".join([f"{self.data[i]}" for i in range(len(self.data) - 1, -1, -1)]) + "]"
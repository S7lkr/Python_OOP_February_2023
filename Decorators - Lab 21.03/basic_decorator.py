# Decorator - a tool allowing to change/extend other function's functionality, without changing its original code

def shopping_decorator(func):
    alcohol = ["beer", "whiskey", "rum", "vodka", "bourbon", "wine"]

    def wrapper(name, age, product, quantity):
        if age < 18 and product in alcohol:
            raise Exception(f"{name} is underage and cannot buy this product!")
        return f"{name} successfully bought {quantity} {product}/s."
    return wrapper


@shopping_decorator
def shopping(name, age, product, quantity):
    return f"{name} of age {age} bought {quantity} {product}/s."


client1 = shopping("Kevin", 16, "beer", 2)
print(client1)

client2 = shopping("Megan", 12, "peanut pack", 1)
print(client2)
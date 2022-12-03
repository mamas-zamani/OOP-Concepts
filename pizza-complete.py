from math import pi   # import the PI constant


class Pizza:
    @property
    def price(self): return 5.00 + 0.05 * self.area + 0.50 * len(self.toppings)

    def add_topping(self, topping):
        if isinstance(topping, str):
            self.toppings.append(topping)
        elif isinstance(topping, (list, tuple)):
            self.toppings.extend(topping)

    @property
    def toppings(self):
        if not hasattr(self, "_toppings"):
            self._toppings = []
        return self._toppings

    def __str__(self):
        return f'{self.toppings if self.toppings else "no toppings"}'


class RoundPizza(Pizza):
    def __init__(self, diameter):
        self.diameter = diameter

    @property
    def diameter(self): return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        if not isinstance(diameter, (int, float)):
            raise TypeError("The diameter must be an integer or float")
        elif diameter < 0:
            raise ValueError("The diameter must not be megative")
        else:
            self._diameter = diameter

    @property
    def area(self): return pi * self.radius ** 2

    @property
    def radius(self): return self.diameter / 2

    def __str__(self):
        return f'{self.diameter}" round pizza with {super().__str__()}'


class SquarePizza(Pizza):
    def __init__(self, length):
        self.length = length

    @property
    def length(self): return self._length

    @length.setter
    def length(self, length):
        if not isinstance(length, (int, float)):
            raise TypeError("The length must be an integer or float")
        elif length < 0:
            raise ValueError("The length must not be megative")
        else:
            self._length = length

    @property
    def area(self):
        return self.length ** 2

    def __str__(self):
        return f'{self.length}" square pizza with {super().__str__()}'


class Coke:
    def __init__(self, ounces):
        self.ounces = ounces

    @property
    def price(self):
        return 1.00 + 0.02 * self.ounces

    def __str__(self):
        return f"{self.ounces}oz Coke"


class Salad:

    @property
    def price(self):
        return 11.95

    def __str__(self):
        return f"Mediterranean Salad"
    

pizza1 = RoundPizza(16)
pizza1.add_topping("Extra Cheese")
pizza2 = SquarePizza(16)
pizza2.add_topping(["Extra Cheese", "Tomato", "Olives"])
order = (pizza1, pizza2, Coke(20), Salad())

for item in order:
    print(f"A {item} will cost ${item.price:.2f}")
else:
    total_price = sum(item.price for item in order)
    print(f"The total order will cost ${total_price:.2f}")

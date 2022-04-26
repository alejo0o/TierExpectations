from functools import reduce, partial
import math


class Calculator:
    pi:float = 3.1416

    def __init__(self, a: int, b: int) -> None:
        self._a = a
        self._b = b
        
    # can be called without an instance
    # knows about class attributes but nothing
    # about instance attributes
    @classmethod
    def multiply_pi(cls,number: int)-> float:
        return number * cls.pi
        

    @property
    def a(self):
        return self.a

    @a.setter
    def a(self, a):
        self.a = a

    @property
    def b(self):
        return self.b

    @b.setter
    def b(self, b):
        self.b = b

    @property
    def sum(self):
        return self.a + self.b

    # can be called without creating an instance of a class
    # and knows nothing of the class attributes
    @staticmethod
    def multiply_values(values):
        return reduce(lambda x, y: x * y, values)

    @staticmethod
    def pow(a, b):
        return math.pow(a, b)


if __name__ == "__main__":
    # Create instance
    calculator = Calculator(3, 2)
    # print(calculator.sum_values()) // throws error
    print("Value pow using partial functions:")
    fn_partial = partial(calculator.pow, 3)
    print(fn_partial(4))  # 81
    print("Multiply n values using static methods")
    print(calculator.multiply_values([1,2,3,4,5]))
    print("Create new object using @classmethod")
    print(Calculator.multiply_pi(3))

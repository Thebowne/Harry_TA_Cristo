from abc import ABC, abstractmethod


class Vehicle(ABC):
    """A class for vehicles"""

    def __init__(self, model, regis_num):
        self._model = model
        self.__regis_num = regis_num

    """This is example of abstract method in OOP"""
    @abstractmethod
    def mileage(self, kilometers):
        pass

    @abstractmethod
    def brand(self, brand):
        pass

    """This example of encapsulation in OOP"""
    """A protected attribute defined by _"""

    def get_model(self):
        return f'Car model: {self._model}'

    """A private attribute defined by __"""

    def get_regis_num(self):
        return f'Registration number: {self.__regis_num}'


class Car(Vehicle):
    """Using the Abstract method to call the variables"""

    def mileage(self, kilometers):
        return f'The mileage for this vehicle: {kilometers} KM'

    def brand(self, brand):
        return f'The model is {brand}'


"""This is an example of inheritance in OOP"""


class Engine:
    def __init__(self, fuel):
        self.fuel = fuel

    def eng_type(self):
        print("This is a:")


class Gas(Engine):
    def __init__(self, fuel):
        super().__init__(fuel)

    def eng_type(self):
        super().eng_type()
        print("Gas car")


class Electric(Engine):
    def __init__(self, fuel):
        super().__init__(fuel)

    def eng_type(self):
        super().eng_type()
        print("Electric car")


class Price:
    def real_prc(self):
        pass


"""Polymorphism method"""
class Second_hand(Price):
    def __init__(self, or_price, depreciation):
        self.or_price = or_price
        self.depreciation = depreciation

    def real_prc(self):
        return f'The price: ${self.or_price - self.depreciation}'


"testing inheritance method"
eng = Gas("Petrol")
eng.eng_type()

x = Car("RS7", "DER3123")


"""testing encapsulation method"""

print(x._model)

"This does not work because it is a private class and cannot be accessed this way"
# print(x.__regis_num)

print(x.get_model())
print(x.get_regis_num())


"testing abstract method"
print(x.mileage(1210.1))
print(x.brand("Audi"))

"testing polymorphism"
y = Second_hand(134000, 25000)
print(y.real_prc())

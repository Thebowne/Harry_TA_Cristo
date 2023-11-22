class House:
    """House class"""

    total_house = 0

    def __init__(self, floors, doors, windows, color="white", address="", has_garage=False):
        self.floors = floors
        self.doors = doors
        self.windows = windows
        self.color = color
        self.address = address
        self.has_garage = has_garage

        House.total_house += 1

    def display_info(self):

        print("House Information: ")
        print(f"    - Address: {self.address}")
        print(f"    - Doors: {self.doors}")
        print(f"    - Floors: {self.floors}")
        print(f"    - Windows: {self.windows}")
        print(f"    - Color: {self.color}")
        print(f"    - Has Garage: {'Yes' if self.has_garage else 'No'}")

    @classmethod
    def house_num(cls):
        print(f'Number of house: {cls.total_house}')

    @staticmethod
    def house_validate(house):
        if not isinstance(house, House):
            return False
        if not all((atrb, int) and atrb > 0 for atrb in (house.floors, house.doors, house.windows)):
            return False

        return True

    """Paint_house, add_garage, Set_address"""
    def paint_house(self, new_color):
        self.color = new_color
        print("Color of ", self, "is", new_color)

    def add_garage(self):
        if self.has_garage:
            print(self, "House already has a garage")
        else:
            self.has_garage = True
            print("A garage has been added to", self)

    def set_address(self, new_address):
        self.address = new_address
        print("The new address of ", self, "is", new_address)

    """__________________________________________________________________"""


house1 = House(floors=2, doors=3, windows=6, color="Blue", has_garage=True, address="123 Main St")
house2 = House(floors=1, doors=2, windows=4, address="123 Main St")

house1.display_info()
house2.display_info()
House.house_num()


house1.paint_house("Blue")
house1.add_garage()
house2.add_garage()
house1.set_address("Boulevard 23")


class Car:
    def __init__(self, brand, model, year, price, type):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.type = type

    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def print_info(self):
        return f"{self.make} {self.model} {self.year} {self.price} {self.type}"

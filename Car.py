
class Car:
    def __init__(self, brand, model, year, price, type):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__price = price
        self.__type = type

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_type(self):
        return self.__type

    def set_type(self, type):
        self.__type = type

    def print_info(self):
        return f"{self.__brand} {self.__model} {self.__year} {float(self.__price):,.2f} {self.__type}"

from Car import Car

class import_car(Car):
    def __init__(self, brand, model, year, price, type, country, tax):
        super().__init__(brand, model, year, price, type)
        self.__country = country
        self.tax = tax

    def get_country(self):
        return self.__country

    def set_country(self, country):
        self.__country = country

    def get_tax(self):
        return self.tax

    def set_tax(self, tax):
        self.tax = tax

    """ When trying to write the file, there seems to reference the object memory location itself, hence __str__ method is needed to convert them into human readabale format."""
    def print_info(self):
        return super().print_info() + f" {self.__country} {self.tax}%"

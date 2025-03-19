from Car import Car

class import_car(Car):
    def __init__(self, brand, model, year, price, type, country, tax):
        super().__init__(brand, model, year, price, type)
        self.country = country
        self.tax = tax

    def get_country(self):
        return self.country

    def set_country(self, country):
        self.country = country

    def get_tax(self):
        return self.tax

    def set_tax(self, tax):
        self.tax = tax

    def print_info(self):
        pass

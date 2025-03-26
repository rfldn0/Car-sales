class Car:
    def __init__(self, make, model, year, price, category):
        self.make = make
        self.model = model
        self.year = int(year)
        self.price = float(price)
        self.category = category

    def display_info(self):
        return f"{self.make:<10} {self.model:<12} {self.year:<6} {self.price:,.2f}   {self.category:<8}"

class ImportCar(Car):
    def __init__(self, make, model, year, price, category, country, tax):
        super().__init__(make, model, year, price, category)
        self.country = country
        self.tax = int(tax)

    def update_tax(self):
        if self.country == "Japan":
            self.tax += 5

    def display_info(self):
        return super().display_info() + f" {self.country:<10} {self.tax}%"

class DomesticCar(Car):
    def __init__(self, make, model, year, price, category, state):
        super().__init__(make, model, year, price, category)
        self.state = state

    def increase_price(self):
        self.price *= 1.15

    def display_info(self):
        return super().display_info() + f" {self.state:<5}"

def read_cars_from_file(filename):
    cars = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split()
                if data[0] == "I":
                    cars.append(ImportCar(*data[1:]))
                elif data[0] == "D":
                    cars.append(DomesticCar(*data[1:]))
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    return cars

def display_cars(cars, title):
    print(title)
    print("=" * 60)
    for car in cars:
        print(car.display_info())
    print()

def update_prices_and_taxes(cars):
    for car in cars:
        if isinstance(car, DomesticCar):
            car.increase_price()
        elif isinstance(car, ImportCar):
            car.update_tax()

def filter_cars_by_price(cars, max_price):
    filtered = [car for car in cars if car.price <= max_price]
    return sorted(filtered, key=lambda x: x.price)

# Main Execution
cars_in_stock = read_cars_from_file("carsInStock.txt")
display_cars(cars_in_stock, "Initial Stock of Cars")

cars_expected = read_cars_from_file("carsExpectedToArrive.txt")
cars_in_stock.extend(cars_expected)
display_cars(cars_in_stock, "Updated Stock with Expected Arrivals")

update_prices_and_taxes(cars_in_stock)
display_cars(cars_in_stock, "Final Stock After Price & Tax Updates")

filtered_cars = filter_cars_by_price(cars_in_stock, 15000)
display_cars(filtered_cars, "Cars Priced Below $15,000")

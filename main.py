# Project No.:  Project 04
# Author: Victor R Tabuni
# Description: Cars, inheritance, polymorphism, overriding, 

#imports
from ImportCar import import_car as i_car
from DomesticCar import domestic_car as d_car
from Car import Car


def display_cars(cars_category, title): 
    print(title)
    print("=" * 60 + "\n")
    for cars_category in cars_category: 
        print(cars_category.print_info())
    print()

def read_data(domestic, imports, filename): 
    with open(filename, "r") as file:
           for line in file:
               data = line.strip().split() #strip the newline character and split the following data into lists
               if line[0] == "D":
                   domestic.append(d_car(*data[1:]))
               elif line[0] == "I":
                    imports.append(i_car(*data[1:]))
    return domestic, imports

def write_data(domestic, imports, filename):
    with open(filename, "w") as file:
        file.write("Imported Cars: \n")
        for car in imports:
            file.write(f"{car.print_info()} \n")
        file.write("\nDomestic Cars: \n")
        for car in domestic:
            file.write(f"{car.print_info()} \n")

def numbers(domestics, imports):
    print(f"Number of imported cars = {len(imports)}")
    print(f"Number of domestic cars = {len(domestics)}")
    print(f"Total = {len(imports) + len(domestics)}\n")

def calculate_total_price(cars):
    total_price = 0
    for car in cars:
        sales_price = car.get_price() * 1.06

        if isinstance(car, i_car):
            total_price += sales_price * (1 + car.get_tax()/100)
        else:
            total_price += sales_price

    return total_price

def filter_price(price, domestics, imports): 
    cars = domestics + imports
    total_price = 0

    #calculate total price
    total_price = calculate_total_price(cars)


    print(f"Filter price less than: {price}")
    # Filter and sort at the same time
    filtered_sorted = sorted(
        [car for car in cars if car.get_price() < price], 
        key=lambda x: x.get_price(),
        reverse=True  # Ascending order (set to True for descending order) IDK what happened, when I set it to True it sorted in ascending order
    )
    
    
    # Output the filtered and sorted list
    for car in filtered_sorted:
        print(car.print_info())
    
    # the amount of cars
    print(f"Number of cars: {len(filtered_sorted)}")
    print(f"Total price of cars in the Stock: ${total_price:,.2f}")


def main():
   dom_cars = []
   imp_cars = []

   try:
       
       print("Welcome to Domestic/Imported Cars Application")
       print("\nStep One: ")
       filename = input("Please enter a file name (with information about Cars in Stock): ") 
       print(f"Input file name for Cars in Stock: {filename}")
       
       read_data(dom_cars, imp_cars, filename)
       write_data(dom_cars, imp_cars, "carsCategoryWise.txt")

       #read the file from carsCategoryWise and present them on CLI
       display_cars(imp_cars, "Imported Cars: ")
       display_cars(dom_cars, "Domestic Cars: ")

       #numbers 
       numbers(dom_cars, imp_cars)

       #STEP 2
       print("Step Two")
       file2 = input("Please enter a file name (with information about Cars expected to arrive): ")
       print(f"Input file name for Cars expected to arrive: {file2}\n")
       #add the cars from carsExpectedToArrive.txt file to the existing list
       read_data(dom_cars, imp_cars, "carsExpectedToArrive.txt")
       
       #display the new cars appended 
       display_cars(imp_cars, "Imported Cars: ")
       display_cars(dom_cars, "Domestic Cars: ")

       #numbers
       numbers(dom_cars, imp_cars)

       #STEP 3
       
       print("Step Three\n")
       #update price and tax 
       for car in imp_cars: 
           car.additional_tax()
       for car in dom_cars: 
           car.update_price()

       #display the new cars appended 
       display_cars(imp_cars, "Imported Cars: ")
       display_cars(dom_cars, "Domestic Cars: ")

       """Note: this new appended cars have not yet been added to the carsCategoryWise.txt file"""

       #numbers
       numbers(dom_cars, imp_cars)

       #print the filtered cars
       filter_price(15000.0, dom_cars, imp_cars)


   except FileNotFoundError:
       print("File not found!")



if __name__ == '__main__':
    main()


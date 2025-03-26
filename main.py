from ImportCar import import_car as i_car
from DomesticCar import domestic_car as d_car

def display_cars(cars_category, title): 
    print(title)
    print("=" * 60)
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



def main():
   dom_cars = []
   imp_cars = []

   try:
       
       read_data(dom_cars, imp_cars, "carsInStock.txt")
       write_data(dom_cars, imp_cars, "carsCategoryWise.txt")

       #read the file from carsCategoryWise and present them on CLI
       display_cars(imp_cars, "Imported Cars: ")
       display_cars(dom_cars, "Domestic Cars: ")

       #numbers 
       print(f"Number of imported cars = {len(imp_cars)}")
       print(f"Number of domestic cars = {len(dom_cars)}")
       print(f"Total = {len(imp_cars) + len(dom_cars)}")

       #add the cars from carsExpectedToArrive.txt file to the existing list
       read_data(dom_cars, imp_cars, "carsExpectedToArrive.txt")

       #display the new cars appended 
       display_cars(imp_cars, "Imported Cars: ")
       display_cars(dom_cars, "Domestic Cars: ")

       """Note: this new appended cars have not yet been added to the carsCategoryWise.txt file"""

   except FileNotFoundError:
       print("File not found")





if __name__ == '__main__':
    main()


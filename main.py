from ImportCar import import_car
from DomesticCar import domestic_car

def main():
   dom_cars = []
   imp_cars = []

   try:
       with open("carsInStock.txt", "r") as file:
           for line in file:
               data = line.strip().split()
               if line[0] == "D":
                   dom_cars.append(domestic_car(*data[1:]))
               elif line[0] == "I":
                    imp_cars.append(import_car(*data[1:]))

        #
        write_data(dom_cars, imp_cars)

   except FileNotFoundError:
       print("File not found")

def write_data(domestic, imports):
    with open("carsCategoryWise.txt") as file:
        file.write("Imported Cars: \n")
        for car in imports:
            file.write(str(car) + "\n")
        file.write("Domestic Cars: \n")
        for car in domestic:
            file.write(str(car) + "\n")



if __name__ == '__main__':
    main()


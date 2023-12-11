class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        current_year = 2023
        if year <= current_year:
            self.year = year
        else:
            print("Invalid year")

    def display_info(self, type):
        return f"{type}: {self.year} {self.make} {self.model}"

    def calculate_mileage(self):
        pass  

    def calculate_towing_capacity(self):
        pass  

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def calculate_mileage(self, distance, consumption):
        return distance / consumption

    def calculate_towing_capacity(self):
        return 3500

class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def calculate_mileage(self, distance, consumption):
        return distance / consumption

    def calculate_towing_capacity(self):
        return 0

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity  # kg

    def calculate_mileage(self, distance, consumption):
        return distance / consumption
    
    def calculate_towing_capacity(self):
        return self.towing_capacity

def main():
    car = Car(make="Toyota", model="Camry", year=2022)
    print(f"{car.display_info('car')} Mileage: {car.calculate_mileage(150,20)} km/l")
    print(f"Towing Capacity: {car.calculate_towing_capacity()} kg")

    motorcycle = Motorcycle(make="Harley-Davidson", model="Sportster", year=2022)
    print(f"{motorcycle.display_info('motorcyle')} Mileage: {motorcycle.calculate_mileage(100,20)} km/l")
    print(f"Towing Capacity: {motorcycle.calculate_towing_capacity()} kg")

    truck = Truck(make="Ford", model="F-150", year=2022, towing_capacity=8000)
    print(f"{truck.display_info('truck')} Towing Capacity: {truck.calculate_towing_capacity()} kg")

if __name__ == "__main__":
    main()
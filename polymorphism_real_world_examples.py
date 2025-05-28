class Vehicle:
    def start_engine(self):
        raise NotImplementedError("Subclasses must implement this method")
    

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"
    
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"
    

class Truck(Vehicle):
    def start_engine(self):
        return "Truck engine started"
    

def get_all_even_numbers(*numbers):
    return [num for num in numbers if num % 2 == 0]


if __name__ == "__main__":
    vehicles = [Car(), Motorcycle(), Truck()]
    
    for vehicle in vehicles:
        print(vehicle.start_engine())
        
    # Demonstrating polymorphism with a function
    def start_all_engines(vehicles):
        for vehicle in vehicles:
            print(vehicle.start_engine())
    
    start_all_engines(vehicles)

    # overloading example
    print(get_all_even_numbers(1, 2, 3, 4, 5, 6))
    print(get_all_even_numbers(10, 15, 20, 25))
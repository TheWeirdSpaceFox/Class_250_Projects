from src.car import Car
def create_car():
    """
    Create an instance of a car where the model year is > 1886 and the color is "Blue"

    return: an instance of a car as specified above
    """

    return Car("volkswagan", "GTI", 2018, "Blue")


def dealership_inventory():
    """
    Make a list of at least 5 cars and return that list

    return: a list with at least 5 cars
    """
    cars = []
    car1 = Car("Honda", "Civic", 2008, "Grey")
    car2 = Car("Ford", "Fusion", 2020, "White")
    car3 = Car("Ford", "Mass", 1903, "Blue")
    car4 = Car("Toyota", "Mass", 1948, "Purple")
    car5 = Car("Lamborghini", "Luxury", 1937, "Black")
    cars.append(car1)
    cars.append(car2)
    cars.append(car3)
    cars.append(car4)
    cars.append(car5)
    return cars

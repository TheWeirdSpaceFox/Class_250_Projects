class Car:
    def __init__(self, make, model, year, color, price=0.0, drivetrain='fwd'):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.drivetrain = drivetrain

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.color}, ${self.price:.02f}, {self.drivetrain})"

if __name__ == '__main__':
    car1 = Car("Honda", "Civic", 1996, "Blue", 10000)
    car2 = Car("Ferrari", "288 GTO", 1984, "Red", 50000, "rwd")
    cars = [car1, car2]
    for car in cars:
        print(car)



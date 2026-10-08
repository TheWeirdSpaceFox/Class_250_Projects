"""
Define class to hold planet data
"""
import math
class Planet:

    # Define class attribute to hold gravitational constant G
    # Style schmile; G demands a capital G
    __G = 6.67408E-11  #m^3 kg^(-1) s^(-2)

    # initialize given name, radius, and mass
    # Define 3 private instance variables for
    #   string name
    #   float radius # average radius in meters
    #   float mass   # mass in kg
    def __init__(self, string, radius, mass):
        self.string = string
        self.radius = float(radius)
        self.mass = float(mass)


    # Define the following methods:

    # __str__()
    # Where string is:
    #  name  radius=<value> m; mass=<value> kg; density=<value> kg/m^3; surface=<value> m^2; g=<value> m/s^2
    # e.g, "Earth radius = 6378100.0 m; mass = 5.97219e+24 kg; volume=1.0868324119376286e+21 m^3; density = 5495.042229512322 kg / m ^ 3;
    #       surface area = 511201962310544.9 m ^ 2; g = 9.798111466947612 m / s ^ 2"
    def get_name(self):
        return self.string
    # get_name() # where name is an instance attribute

    def get_radius(self):
        return self.radius
    # get_radius() # where radius is an instance attribute

    def get_mass(self):
        return self.mass
    # get_mass() # where mass is an instance attribute

    def get_volume(self):
        self.volume = (4./3)*(math.pi*pow(self.radius, 3))
        return self.volume
    # get_volume() #where volume = (4./3)*math.pi*pow(self.__radius, 3)

    def get_density(self):
        volume = Planet.get_volume(self)
        self.density = self.mass/(self.volume)
        return self.density
    # get_density()  # where density = mass/volume

    def get_surface_area(self):
        self.surface_area = (4*math.pi)*(math.pow(self.radius, 2))
        return self.surface_area
    # get_surface_area() # where surface area = 4*math.pi*math.pow(self.__radius, 2)

    def get_gravity(self):
        self.gravity = (Planet.__G*self.mass)/(math.pow(self.radius, 2))
        return self.gravity
    # get_gravity() # acceleration due to gravity at surface, where Gravity = Planet.__G*self.__mass/math.pow(self.__radius, 2)
    #  see http://www.softschools.com/formulas/physics/acceleration_due_to_gravity_formula/54/

    def __str__(self):
        density = Planet.get_density(self)
        surface_area = Planet.get_surface_area(self)
        gravity = Planet.get_gravity(self)
        volume = Planet.get_volume(self)
        return "{} radius = {} m; mass = {} kg; volume = {}; density = {} kg/m^3; surface area = {} m^2; g = {} m/s^2".format(self.string, self.radius, self.mass,volume, density, surface_area, gravity)
    # Get string using __str__ that shows:
    #  name  radius=<value> m; mass=<value> kg; volume=1.0868324119376286e+21 m^3; density=<value> kg/m^3; surface=<value> m^2; g=<value> m/s^2


if __name__ == '__main__':
    print(Planet("Earth", 6.3781e6, 5.97219e24))

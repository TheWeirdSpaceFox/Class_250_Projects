import csv
import os
from src.homework.planets.planet import Planet

#Note: Be sure you set your run configuration properly it should be at the project folder (w9-inheritance-polymorphism-f21)

def generate_planet_list(file_path):
    """
    Read in the data from data/planets.txt (ignoring comment lines)
    construct a list of Planet instances and return the list of planets.
    When reading in the file ignore lines that start with '#' as they are comment lines.

    The file contains diameter in kilometers, but the planet constructor expects diameter in meters.
      Make sure you do the conversion (recall that 1 kilometer = 1000 meters)

    :param file_path:
    :return planets: Return a list of planet objects
    """
    with open(file_path) as file:
        file = file.readlines()
        i = 0
        name = []
        radius = []
        mass = []
        final_list = []
        for line in file:
            if i == 0 or i == 1:
                i += 1
            else:
                line = line.split(',')
                name.append(line[0])
                radius.append(float(line[1]))
                mass.append(line[2])
        for num in range(len(name)):
            final_list.append(Planet(name[num], radius[num]*1000, mass[num]))
    return final_list


if __name__ == '__main__':
    file_path = os.path.join("data", "planets.txt")
    planets = generate_planet_list(file_path)

    print("Look a list of planet objects: ")
    print(planets)
    print("\n")

    print("\n\nPlanet data:")
    for planet in planets:
        print(planet.get_density(), end=",")

    #Add a new planet, Planet X, radius = 3000km, mass = 2.7e23
    planet_x = Planet("Planet X", 3000*1000, 2.7e23)
    planets.append(planet_x)

    for planet in planets:
        print(planet)





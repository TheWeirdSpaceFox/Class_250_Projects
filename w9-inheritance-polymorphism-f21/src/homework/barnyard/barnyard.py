from src.homework.barnyard.farm_animal import FarmAnimal
from src.homework.barnyard.hen import Hen
from src.homework.barnyard.rooster import Rooster
from src.homework.barnyard.duck import Duck
from src.homework.barnyard.goat import Goat
from src.homework.barnyard.cow import Cow


def get_barnyard():
    """
    Return a list of animals as described in README
    :return : list of animal instances
    """
    Hen1 = Hen(0.25)
    Hen2 = Hen(0.6)
    Hen3 = Hen(1.0)
    Hen4 = Hen(8)
    Rooster1 = Rooster(0.25)
    Rooster2 = Rooster(0.6)
    Rooster3 = Rooster(1.0)
    Duck1 = Duck(2)
    Goat1 = Goat(4)
    Cow1 = Cow(6)

    animals = []
    animals.append(Hen1)
    animals.append(Hen2)
    animals.append(Hen3)
    animals.append(Hen4)
    animals.append(Rooster1)
    animals.append(Rooster2)
    animals.append(Rooster3)
    animals.append(Duck1)
    animals.append(Goat1)
    animals.append(Cow1)
    #random.shuffle(animals)
    return animals

def get_layers(animals):
    """
    Given list of animals, return ones that can lay eggs
    :param animals: list of animal instances
    :return : list of "layers"
    """
    hens = []
    for animal1 in animals:
        animal = str(animal1).split(",")
        if "Hen" in animal:
            if float(animal[0]) > 0.5 and float(animal[0]) < 7.0:
                hens.append(animal1)
    return hens

def get_roosters(animals):
    """
    Given list of animals, return ones that are roosters
    :param animals: list of animal instances
    :return : list of rooster instances
    """
    rooster = []
    for animal1 in animals:
        animal = str(animal1).split(",")
        for x in animal:
            if x == "Rooster":
                rooster.append(animal1)
    return rooster


def listen(animals):
    """
    Given list of animals, return list of sounds they make
    :param animals: list of animal instances
    :return : list of sounds
    """
    relevant = ["Chicken", "Cow", "Duck", "Goat", "Hen", "Rooster", "Ruminant"]
    sounds = []
    for animal1 in animals:
        animal2 = animal1.make_sound()
        sounds.append(animal2)
        # animal_split = str(animal1).split(",")
        # for x in animal_split:
        #     if x in relevant:
        #         sound = animal1.make_sound()
        #         sounds.append(sound)
    return sounds

if __name__ == '__main__':

    animals = get_barnyard()
    print("All animals:",[str(ani) for ani in animals])
    print(" listen: ",listen(animals))
    print(" Laying hens:", [str(ani) for ani in get_layers(animals)])
    print(" Roosters: ",[str(ani) for ani in get_roosters(animals)])

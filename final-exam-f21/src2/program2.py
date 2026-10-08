"""
Program 2

This program is based on the grocery items defined in the given folder.

You have Grocery, Dairy, Milk, Yogurt, Bread, Loaf, Bagel, Paper, and ToiletPaper as defined.

You also have an Imported class defined in given.

Check the given folder for grocery items.

Write the methods as described below.

    For full credit, you need to write one additional class.
    Plantain, which inherits from BOTH Grocery and Imported
      That is an instance of Plantain is both a Grocery and Imported instance.
      The constructor should parameters of price and origin in that order.

    Plantain should have str( ) conversion function that prints name and price as Grocery item and country of origin.

    Write the class in src2/plantain.py

    If you handle the constructors properly it only requires 6  non-blank lines of code total.


@author Amanda Sanders
 vvvvvvvvvvv you code below here vvvvvvvvvvvvvv
"""
# pylint: disable=C0103

from given.cheese import Cheese
from given.loaf import Loaf
from given.toilet_paper import ToiletPaper
from given.bread import Bread
import numpy as np

def make_shopping_list():
    """
    Create a grocery list with :
        exactly 1 cheese, 1 loaf, and 1 toilet paper items
        Make up your own prices

    :return: a list of grocery items
    """
    cheese = Cheese(1.50)
    loaf = Loaf(2.00)
    toilet_paper = ToiletPaper(20)

    grocery_list = [cheese, loaf, toilet_paper]


    # grocery_list = ["cheese 1.50", "loaf 2.00", "toilet_paper 20"]
    return grocery_list


def bread_total(grocery_list):
    """
    Given list of grocery items, return
    the total cost of Bread items
    :param grocery_list:
    :return: total cost of Bread items
    """
    list = []
    for x in grocery_list:
        if isinstance(x, Bread) or isinstance(x, Loaf):
            x = Bread.__str__(x)
            i = x.split(" ")
            i = i[0]
            bread = x
            bread = bread.split("$")
            bread = bread[1]
            bread = bread.split(")")
            bread = bread[0]
            list.append(float(bread))
    list = np.array(list)
    list = np.cumsum(list)
    if len(list) == 0:
        return 0.0
    else:
        final = list[-1]
        return final


"""
^^^^^^^^^^^^^^^^^^ your code up here ^^^^^^^^^^^^^^^^^^^^ 
I'm giving you the below code as simple test.  Just leave as is
"""
if __name__ == "__main__":
    groceries = make_shopping_list()
    print("grocery list (as string): ", [str(item) for item in groceries])

    print("total cost of bread = ${:.2f}".format(bread_total(groceries)))

    try:
        print("Trying to import Plantain class definition:")
        from src2.plantain import Plantain
    except Exception as e:
        print(" Failed to import Plantain class")
        print(e)


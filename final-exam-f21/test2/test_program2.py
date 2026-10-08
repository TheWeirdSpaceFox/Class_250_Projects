import unittest

from src2 import program2
from given.milk import Milk
from given.bagel import Bagel
from given.cheese import Cheese
from given.loaf import Loaf
from given.yogurt import Yogurt
from given.toilet_paper import ToiletPaper

import random


class TestProgram2(unittest.TestCase):

    def setUp(self):
        items = [Bagel, Loaf, Milk, Cheese, Yogurt,  ToiletPaper]
        self.counts = [random.randint(2,10) for i in range(len(items))]
        self.total_costs = len(items)*[0.0]
        self.grocery_list = []

        for i, type in enumerate(items):
            for cnt in range(self.counts[i]):
                price = int(random.uniform(0.99, 10.99)*100)/100.0
                self.total_costs[i] += price
                #print("price = ", price)
                self.grocery_list.append(type(price))

        self.total_bread = sum(self.total_costs[:2])

    def test_has_plantain(self):
        from src2.plantain import Plantain
        from given.grocery import Grocery

        plantain = Plantain(3.99, "Cuba")
        self.assertIsNotNone(plantain)
        self.assertIsInstance(plantain, Grocery, msg="Plantain must inherit Grocery")

    def test_has_plantain_data(self):

        from src2.plantain import Plantain
        from given.grocery import Grocery
        from given.imported import Imported

        plantain = Plantain(3.99, "Cuba")
        self.assertIsNotNone(plantain)
        self.assertIsInstance(plantain, Grocery, msg="Plantain must inherit Grocery")
        self.assertIsInstance(plantain, Imported, msg="Plantain must inherit Imported")
        self.assertAlmostEqual(3.99, plantain.per_unit_cost(), msg="Plantain must have per unit cost")
        self.assertEqual("Cuba", plantain.origin, msg="Plantain must have origin")

    def test_has_plantain_str(self):

        from src2.plantain import Plantain
        from given.grocery import Grocery
        from given.imported import Imported

        plantain = Plantain(3.99, "Cuba")
        self.assertIsNotNone(plantain)
        self.assertIsInstance(plantain, Grocery, msg="Plantain must inherit Grocery")
        self.assertIsInstance(plantain, Imported, msg="Plantain must inherit Imported")
        self.assertAlmostEqual(3.99, plantain.per_unit_cost(), msg="Plantain must have price")
        self.assertEqual("Cuba", plantain.origin, msg="Plantain must have origin")

        string = str(plantain)
        self.assertTrue("3.99" in string, msg="Plantain string should contain the price")
        self.assertTrue("Cuba" in string, msg="Plantain string should contain the country of origin")
        self.assertTrue("Plantain" in string, msg="Plantain string should contain the class name")

        string2 = str(Plantain(1.99, "India"))
        self.assertTrue("1.99" in string2, msg="Plantain string should contain the price")
        self.assertTrue("India" in string2, msg="Plantain string should contain the country of origin")
        self.assertTrue("Plantain" in string2, msg="Plantain string should contain the class name")


    def test_total_bread_has_total(self):
        cost = program2.bread_total(self.grocery_list)
        self.assertIsNotNone(cost, msg="Must return the total cost")
        self.assertTrue(type(cost) is float, msg="Must return the total cost as float")

    def test_make_shopping_list_is_a_list(self):
        groceries = program2.make_shopping_list()
        self.assertEqual(type(groceries), list, msg="The return type of make_shopping_list() must be a list")

    def test_make_shopping_list_not_empty(self):
        groceries = program2.make_shopping_list()
        self.assertGreater(len(groceries), 0,
                           msg="The length of the grocery list from make_shopping_list() must be non-zero")

    def test_make_shopping_list(self):

        from given.grocery import Grocery
        groceries = program2.make_shopping_list()
        self.assertIsNotNone(groceries, msg="must make a grocery list")
        self.assertIsInstance(groceries, list, msg="must make a grocery list")
        self.assertTrue(len(groceries) > 2, msg="must make a grocery list with some data")

        milk_count = 0
        yog_count = 0
        loaf_count = 0
        bagel_count = 0
        cheese_count = 0
        tp_count = 0

        # exactly 1 cheese, 1 loaf, and 1 toilet paper items
        for item in groceries:
            self.assertIsInstance(item, Grocery, msg="must all be grocery items")
            if isinstance(item, Milk):
                milk_count += 1
            if isinstance(item, Yogurt):
                yog_count += 1
            if isinstance(item, Cheese):
                cheese_count += 1
            if isinstance(item, Loaf):
                loaf_count += 1
            if isinstance(item, Bagel):
                bagel_count += 1
            if isinstance(item, ToiletPaper):
                tp_count += 1

        # exactly 1 cheese, 1 loaf, and 1 toilet paper items
        self.assertFalse(milk_count > 0, msg="Must contain at least one Milk")
        self.assertTrue(tp_count > 0, msg="Must contain at least one ToiletPaper")
        self.assertTrue(cheese_count > 0, msg="Must contain at least one Cheese")
        self.assertTrue(loaf_count > 0, msg="Must contain at least one Bagel")

    def test_make_shopping_list_exact(self):

        from given.grocery import Grocery
        groceries = program2.make_shopping_list()
        self.assertIsNotNone(groceries, msg="must make a grocery list")
        self.assertIsInstance(groceries, list, msg="must make a grocery list")
        self.assertTrue(len(groceries) > 2, msg="must make a grocery list with some data")
        milk_count = 0
        yog_count = 0
        loaf_count = 0
        bagel_count = 0
        cheese_count = 0
        tp_count = 0

        # exactly 1 cheese, 1 loaf, and 1 toilet paper items
        for item in groceries:
            self.assertIsInstance(item, Grocery, msg="must all be grocery items")
            if isinstance(item, Milk):
                milk_count += 1
            if isinstance(item, Yogurt):
                yog_count += 1
            if isinstance(item, Cheese):
                cheese_count += 1
            if isinstance(item, Loaf):
                loaf_count += 1
            if isinstance(item, Bagel):
                bagel_count += 1
            if isinstance(item, ToiletPaper):
                tp_count += 1

        # exactly 1 toilet paper, 1 bagel, and 1 cheese items
        self.assertEqual(0, milk_count, msg="Must contain one Milk")
        self.assertEqual(0, yog_count, msg="Must contain 0 Yogurt")
        self.assertEqual(1, loaf_count, msg="Must contain 1 Loaf")
        self.assertEqual(0, bagel_count, msg="Must contain 0 Bagel")
        self.assertEqual(1, cheese_count, msg="Must contain 1 Cheese")
        self.assertEqual(1, tp_count, msg="Must contain 1 ToiletPaper")

    def test_get_total_bread_only_bread(self):
        cost = program2.bread_total(self.grocery_list[:4])  # At least first 4 items are bread
        self.assertIsNotNone(cost, msg="must return cost")
        self.assertIsInstance(cost, float, msg="must return number cost")
        self.assertAlmostEqual(sum([item.per_unit_cost() for item in self.grocery_list[:4]]), cost, msg="must return total cost of all bread items")

    def test_get_total_bread0(self):
        cost = float(program2.bread_total(self.grocery_list))
        self.assertIsNotNone(cost, msg="must return cost")
        self.assertIsInstance(cost, float, msg="must return number cost")
        self.assertAlmostEqual(self.total_bread, cost, msg="must return total cost of all bread")

    def test_get_total_bread1(self):
        cost = float(program2.bread_total(self.grocery_list))
        self.assertIsNotNone(cost, msg="must return cost")
        self.assertIsInstance(cost, float, msg="must return number cost")
        self.assertAlmostEqual(self.total_bread, cost, msg="must return total cost of all bread")

    def test_get_total_bread2(self):
        cost = float(program2.bread_total(self.grocery_list))
        self.assertIsNotNone(cost, msg="must return cost")
        self.assertIsInstance(cost, float, msg="must return number cost")
        self.assertAlmostEqual(self.total_bread, cost, msg="must return total cost of all bread")

    def test_get_total_bread_no_bread(self):
        print([str(item) for item in self.grocery_list])
        cost = float(program2.bread_total([Cheese(3.99), ToiletPaper(5.99)]))
        self.assertIsNotNone(cost, msg="must return cost")
        self.assertIsInstance(cost, float, msg="must return number cost")
        self.assertAlmostEqual(0.0, cost, msg="must return total cost of all bread items (nothing else)")

    def test_get_total_bread_shuffled(self):
        shuffled = self.grocery_list[:]
        random.shuffle(shuffled)
        cost = float(program2.bread_total(shuffled))
        self.assertIsNotNone(cost, msg="must return cost")
        self.assertIsInstance(cost, float, msg="must return number cost")
        self.assertAlmostEqual(self.total_bread, cost, msg="must return total cost of all bread")



if __name__ == '__main__':
    unittest.main()

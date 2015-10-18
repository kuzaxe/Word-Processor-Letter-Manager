
from stack import *
import unittest

class swapTest(unittest.TestCase):

    def test01_empty_stack(self):
        """ tests if function handles empty stack """
        s = Stack()
        swap(s)
        self.assertEqual(s.items, [], "Test 01 failed in class swapTest")


    def test02_one_item_stack(self):
        """ tests if function handles one item stack """
        s = Stack()
        s.push(1)
        swap(s)
        self.assertEqual(s.items, [1], "Test 02 failed in class swapTest")

    def test03_multiple_item_stack(self):
        """ tests if function handles multiple item stack """
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        swap(s)
        self.assertEqual(s.items, [1, 2, 4, 3], "Test 03 failed in class swapTest")

    def test03_multiple_type_items_stack(self):
        """ tests if function handles multiple types of item stack """
        s = Stack()
        s.push(1)
        s.push("2")
        s.push([3])
        s.push(True)
        swap(s)
        self.assertEqual(s.items, [1, "2", True, [3]], "Test 03 failed in class swapTest")

class rollTest(unittest.TestCase):


    def test01_empty_stack(self):
        """ tests if function handles empty stack """
        s = Stack()
        roll(s, 1)
        self.assertEqual(s.items, [], "Test 01 failed in class rollTest")


    def test02_one_item_stack(self):
        """ tests if function handles one item stack """
        s = Stack()
        s.push(1)
        roll(s, 1)
        self.assertEqual(s.items, [1], "Test 02 failed in class rollTest")

    def test03_multiple_item_stack(self):
        """ tests if function handles multiple item stack """
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        roll(s, 3)
        self.assertEqual(s.items, [1, 3, 4, 2], "Test 03 failed in class rollTest")

    def test04_roll_first_item(self):
        """ tests if function rolls first item correctly """
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        roll(s, 1)
        self.assertEqual(s.items, [1, 2, 3], "Test 04 failed in class rollTest")

    def test05_roll_middle_item(self):
        """ tests if function rolls middle item correctly """
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        roll(s, 2)
        self.assertEqual(s.items, [1, 3, 2], "Test 05 failed in class rollTest")

    def test06_roll_last_item(self):
        """ tests if function rolls last item correctly """
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        roll(s, 3)
        self.assertEqual(s.items, [2, 3, 1], "Test 06 failed in class rollTest")


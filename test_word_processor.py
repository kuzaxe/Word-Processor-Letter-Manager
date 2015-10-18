
import unittest
from word_processor import *
from unittest.mock import patch


class InputTest(unittest.TestCase):

    def test01_input_no_items(self):
        """ Trial: Tests if program ends properly if no item is added to main _stack """
        a = WordProcessor()
        with patch(target='builtins.input', new=lambda i: str("")):
            r = a.main()
        self.assertEqual(None, r, "Test 01 failed in class InputTest")

    def test02_input_one_item(self):
        """ Tests if one item can be added to main _stack """
        a = WordProcessor()
        a.commands('a')
        r = a._stack.items
        self.assertEqual(['a'], r, "Test 02 failed in class InputTest")

    def test03_input_multiple_items(self):
        """ Tests if multiple items can be added to main _stack """
        a = WordProcessor()
        a.commands('a')
        a.commands('b')
        r = a._stack.items
        self.assertEqual(['a', 'b'], r, "Test 03 failed in class InputTest")

    def test04_input_blank_space(self):
        """ Tests if blank space items are handled correctly """
        a = WordProcessor()
        a.commands(' ')
        r = a._stack.items
        self.assertEqual([' '], r, "Test 04 failed in class InputTest")

    def test05_input_non_alpha_chr(self):
        """ Tests if non-alpha characters are handled correctly """
        a = WordProcessor()
        a.commands('23*$@"')
        a.commands('";]|~')
        r = a._stack.items
        self.assertEqual(['23*$@"', '";]|~'], r, "Test 05 failed in class InputTest")


class UndoTest(unittest.TestCase):

    def test01_undo_one_item(self):
        """ Tests if one item can be undone properly """
        a = WordProcessor()
        a.commands('a')
        a.undo()
        r = a._stack.items
        self.assertEqual([], r, "Test 01 failed in class UndoTest")

    def test02_undo_on_empty_stack(self):
        """ Tests if exception is raised when undo on empty list """
        a = WordProcessor()
        self.assertRaises(InputError, a.undo(), "Test 02 failed in class UndoTest")

    def test03_undo_multiple_items(self):
        """ Tests if multiple items can be undone for multi-level undo """
        a = WordProcessor()
        a.commands('a')
        a.commands('b')
        a.undo()
        a.undo()
        r = a._stack.items
        self.assertEqual([], r, "Test 03 failed in class UndoTest")

    def test04_undo_a_delete_one_item_stack(self):
        """ Tests if a delete is properly undone """
        a = WordProcessor()
        a.commands('a')
        a.delete(1)
        a.undo()
        r = a._stack.items
        self.assertEqual(['a'], r, "Test 04 failed in class UndoTest")

    def test05_undo_a_delete_multiple_item_stack(self):
        """ Tests if undo on multiple deletes are placed back in their original index """
        a = WordProcessor()
        a.commands('a')
        a.commands('b')
        a.commands('c')
        a.delete(2)
        a.delete(1)
        a.undo()
        r = a._stack.items
        self.assertEqual(['a', 'c'], r, "Test 05 failed in class UndoTest")


class RedoTest(unittest.TestCase):

    def test01_redo_one_item(self):
        """ Tests if one item is put back in stack """
        a = WordProcessor()
        a.commands('a')
        a.undo()
        a.redo()
        r = a._stack.items
        self.assertEqual(['a'], r, "Test 01 failed in class RedoTest")

    def test02_redo_on_empty_stack(self):
        """ Tests if exception is raised when redo on empty stack """
        a = WordProcessor()
        self.assertRaises(InputError, a.redo(), "Test 02 failed in class RedoTest")

    def test03_redo_multiple_items(self):
        """ Tests if multiple items can be redone for multi-level redo """
        a = WordProcessor()
        a.commands('a')
        a.commands('b')
        a.undo()
        a.undo()
        a.redo()
        a.redo()
        r = a._stack.items
        self.assertEqual(['a', 'b'], r, "Test 03 failed in class RedoTest")

    def test04_redo_a_delete_one_item_stack(self):
        """ Tests if item is placed in designated index after redo-ing a delete """
        a = WordProcessor()
        a.commands('a')
        a.delete(1)
        a.undo()
        a.redo()
        r = a._stack.items
        self.assertEqual([], r, "Test 04 failed in class RedoTest")

    def test05_redo_a_delete_multiple_item_stack(self):
        """ Tests if multiple items are placed in designated index after multi-level redo """
        a = WordProcessor()
        a.commands('a')
        a.commands('b')
        a.commands('c')
        a.delete(2)
        a.delete(1)
        a.undo()
        a.redo()
        r = a._stack.items
        self.assertEqual(['c'], r, "Test 05 failed in class RedoTest")


class DelTest(unittest.TestCase):

    def test01_del_one_item(self):
        """ Tests if one item is deleted properly """
        a = WordProcessor()
        a.commands('a')
        with patch(target='builtins.input', new=lambda i: int(1)):
            a.commands('d')
        r = a._stack.items = []
        self.assertEqual([], r, "Test 01 failed in class DelTest")

    def test02_del_front_item_in_stack(self):
        """ Tests if first item in multiple item stack is deleted properly """
        a = WordProcessor()
        a.commands('a')
        a.commands('b')
        a.commands('c')
        with patch(target='builtins.input', new=lambda i: int(1)):
            a.commands('d')
        r = a._stack.items
        self.assertEqual(['b', 'c'], r, "Test 02 failed in class DelTest")

    def test03_del_middle_item_in_stack(self):
        """ Tests if middle item in multiple item stack is deleted properly """
        a = WordProcessor()
        a.commands('a')
        a.commands('b')
        a.commands('c')
        with patch(target='builtins.input', new=lambda i: int(2)):
            a.commands('d')
        r = a._stack.items
        self.assertEqual(['a', 'c'], r, "Test 03 failed in class DelTest")

    def test04_del_end_item_in_stack(self):
        """ Tests if last item in multiple item stack is deleted properly """
        a = WordProcessor()
        a.commands('a')
        a.commands('b')
        a.commands('c')
        with patch(target='builtins.input', new=lambda i: int(3)):
            a.commands('d')
        r = a._stack.items
        self.assertEqual(['a', 'b'], r, "Test 04 failed in class DelTest")

    def test05_del_on_empty_stack(self):
        """ Tests if exception is thrown for try to delete on empty stack """
        a = WordProcessor()
        self.assertRaises(InputError, a.delete(4), "Test 05 failed in class RedoTest")

    def test06_del_invalid_index(self):
        """ Tests if exception is thrown for try to delete an invalid index """
        a = WordProcessor()
        a.commands('a')
        self.assertRaises(InputError, a.delete(2), "Test 06 failed in class RedoTest")


if __name__ == "__main__":
    unittest.main()

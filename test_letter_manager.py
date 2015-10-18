import unittest

class InitializerTest(unittest.TestCase):

    def test01_multiple_item_string_input(self):
        """ Tests if multiple items are correctly inserted in designated positions """
        a = LetterManager("abcdefghijkl")
        l = [['a'], [1], ['b'], [1], ['c'], [1], ['d'], [1], ['e'], [1], ['f'], [1],
            ['g'], [1], ['h'], [1], ['i'], [1], ['j'], [1], ['k'], [1], ['l'], [1],
            ['m'], [0], ['n'], [0], ['o'], [0], ['p'], [0], ['q'], [0], ['r'], [0],
            ['s'], [0], ['t'], [0], ['u'], [0], ['v'], [0], ['w'], [0], ['x'], [0],
            ['y'], [0], ['z'], [0], ]
        self.assertEqual(a.alpha_counter, l, "Test 01 failed in class InitializerTest")

    def test02_empty_string_input(self):
        """ Tests if program handles empty string correctly without error """
        a = LetterManager("")
        l = [['a'], [0], ['b'], [0], ['c'], [0], ['d'], [0], ['e'], [0], ['f'], [0],
            ['g'], [0], ['h'], [0], ['i'], [0], ['j'], [0], ['k'], [0], ['l'], [0],
            ['m'], [0], ['n'], [0], ['o'], [0], ['p'], [0], ['q'], [0], ['r'], [0],
            ['s'], [0], ['t'], [0], ['u'], [0], ['v'], [0], ['w'], [0], ['x'], [0],
            ['y'], [0], ['z'], [0], ]
        self.assertEqual(a.alpha_counter, l, "Test 02 failed in class InitializerTest")

    def test03_multiple_item_string_input_with_uppercase(self):
        """ Tests if initializer handles uppercase/lowercase letters correctly """
        a = LetterManager("abCdEfGHiJKl")
        l = [['a'], [1], ['b'], [1], ['c'], [1], ['d'], [1], ['e'], [1], ['f'], [1],
            ['g'], [1], ['h'], [1], ['i'], [1], ['j'], [1], ['k'], [1], ['l'], [1],
            ['m'], [0], ['n'], [0], ['o'], [0], ['p'], [0], ['q'], [0], ['r'], [0],
            ['s'], [0], ['t'], [0], ['u'], [0], ['v'], [0], ['w'], [0], ['x'], [0],
            ['y'], [0], ['z'], [0], ]
        self.assertEqual(a.alpha_counter, l, "Test 03 failed in class InitializerTest")

    def test04_multiple_item_string_input_w_spaces_punct(self):
        """ Tests if initializer handles punctuation and spaces correctly """
        a = LetterManager("abc; def2gh ijk'l!#")
        l = [['a'], [1], ['b'], [1], ['c'], [1], ['d'], [1], ['e'], [1], ['f'], [1],
            ['g'], [1], ['h'], [1], ['i'], [1], ['j'], [1], ['k'], [1], ['l'], [1],
            ['m'], [0], ['n'], [0], ['o'], [0], ['p'], [0], ['q'], [0], ['r'], [0],
            ['s'], [0], ['t'], [0], ['u'], [0], ['v'], [0], ['w'], [0], ['x'], [0],
            ['y'], [0], ['z'], [0], ]
        self.assertEqual(a.alpha_counter, l, "Test 04 failed in class InitializerTest")

    def test05_one_item_string_input(self):
        """ Tests if program handles one item string correctly without error """
        a = LetterManager("f")
        l = [['a'], [0], ['b'], [0], ['c'], [0], ['d'], [0], ['e'], [0], ['f'], [1],
            ['g'], [0], ['h'], [0], ['i'], [0], ['j'], [0], ['k'], [0], ['l'], [0],
            ['m'], [0], ['n'], [0], ['o'], [0], ['p'], [0], ['q'], [0], ['r'], [0],
            ['s'], [0], ['t'], [0], ['u'], [0], ['v'], [0], ['w'], [0], ['x'], [0],
            ['y'], [0], ['z'], [0], ]
        self.assertEqual(a.alpha_counter, l, "Test 05 failed in class InitializerTest")


class GetTest(unittest.TestCase):

    def test01_get_a_letter(self):
        """ Tests if multiple items are correctly inserted in designated positions """
        a = LetterManager("aabcd")
        self.assertEqual(a.Get("a"), 2, "Test 01 failed in class GetTest")

    def test02_test_invalid_input_int(self):
        """ Tests if exception is raised when invalid (int) input is given """
        a = LetterManager("abc")
        self.assertRaises(InputError, a.Get(1), "Test 02 failed in class GetTest")

    def test03_test_invalid_input_nonalpha_str(self):
        """ Tests if exception is raised when invalid (str(int)) input is given """
        a = LetterManager("abc")
        self.assertRaises(InputError, a.Get("1"), "Test 03 failed in class GetTest")

    def test04_get_few_letters(self):
        """ Tests if input with more than one letter is handled correctly """
        a = LetterManager("aabcd")
        self.assertRaises(InputError, a.Get('bc'), "Test 04 failed in class GetTest")

    def test05_empty_parameter(self):
        """ Tests if input with more than one letter is handled correctly """
        a = LetterManager("aabcd")
        self.assertRaises(InputError, a.Get(''), "Test 05 failed in class GetTest")


class SetTest(unittest.TestCase):

    def test01_set_a_letter_to_value(self):
        """ Tests if method sets the give value to the given letter """
        a = LetterManager("abcd")
        a.Set("a", 2)
        self.assertEqual(a.Get("a"), 2, "Test 01 failed in class SetTest")

    def test02_test_invalid_input_int(self):
        """ Tests if exception is raised when invalid input (int, int) is given """
        a = LetterManager("abc")
        self.assertRaises(InputError, a.Set(1, 1), "Test 02 failed in class SetTest")

    def test03_test_invalid_input_str(self):
        """ Tests if exception is raised when invalid input (int, str) is given  """
        a = LetterManager("abc")
        self.assertRaises(InputError, a.Set(1, "a"), "Test 03 failed in class SetTest")

    def test04_test_invalid_input_str(self):
        """ Tests if exception is raised when invalid input (str, str) is given  """
        a = LetterManager("abc")
        self.assertRaises(InputError, a.Set("1", "a"), "Test 04 failed in class SetTest")

    def test05_empty_parameters(self):
        """ Tests if exception is raised when invalid input (str, str) is given  """
        a = LetterManager("abc")
        self.assertRaises(InputError, a.Set("", 1), "Test 05 failed in class SetTest")


class SizeTest(unittest.TestCase):

    def test01_get_size_without_inventory_mods(self):
        """ Tests if total number of letters in inventory is returned """
        a = LetterManager("abcd")
        self.assertEqual(a.Size(), 4, "Test 01 failed in class SizeTest")

    def test02_get_size_with_inventory_mods_sizeup(self):
        """ Tests if total number of letters in inventory is returned (with modification of inventory)"""
        a = LetterManager("abcd")
        a.Set("a", 3)
        self.assertEqual(a.Size(), 6, "Test 02 failed in class SizeTest")

    def test03_empty_inventory(self):
        """ Tests if total number of letters in inventory is returned"""
        a = LetterManager("")
        self.assertEqual(a.Size(), 0, "Test 03 failed in class SizeTest")

    def test04_get_size_with_inventory_mods_sizedown(self):
        """ Tests if total number of letters in inventory is returned"""
        a = LetterManager("abcd")
        a.Set("a", 0)
        self.assertEqual(a.Size(), 3, "Test 04 failed in class SizeTest")


class IsEmptyTest(unittest.TestCase):

    def test01_inventory_without_items(self):
        """ Tests if total number of letters in inventory is returned """
        a = LetterManager("")
        self.assertEqual(a.IsEmpty(), True, "Test 01 failed in class IsEmptyTest")

    def test02_inventory_with_items(self):
        """ Tests if total number of letters in inventory is returned (with modification of inventory)"""
        a = LetterManager("abcd")
        self.assertEqual(a.IsEmpty(), False, "Test 02 failed in class IsEmptyTest")


class StrTest(unittest.TestCase):

    def test01_inventory_without_items(self):
        """ Tests if total number of letters in inventory is returned """
        a = LetterManager("")
        self.assertEqual(str(a), "[]", "Test 01 failed in class StrTest")

    def test02_inventory_with_one_item(self):
        """ Tests if total number of letters in inventory is returned (with modification of inventory)"""
        a = LetterManager("a")
        self.assertEqual(str(a), "[a]", "Test 02 failed in class StrTest")

    def test03_inventory_with_multiple_items(self):
        """ Tests if total number of letters in inventory is returned (with modification of inventory)"""
        a = LetterManager("abcd")
        self.assertEqual(str(a), "[abcd]", "Test 03 failed in class StrTest")


class AddTest(unittest.TestCase):

    def test01_add_different_items(self):
        """ Tests if lists with different items add correctly"""
        a = LetterManager("abcdef")
        b = LetterManager("ghijkl")
        l = [['a'], [1], ['b'], [1], ['c'], [1], ['d'], [1], ['e'], [1], ['f'], [1],
            ['g'], [1], ['h'], [1], ['i'], [1], ['j'], [1], ['k'], [1], ['l'], [1],
            ['m'], [0], ['n'], [0], ['o'], [0], ['p'], [0], ['q'], [0], ['r'], [0],
            ['s'], [0], ['t'], [0], ['u'], [0], ['v'], [0], ['w'], [0], ['x'], [0],
            ['y'], [0], ['z'], [0], ]
        self.assertEqual(a.Add(b).alpha_counter, l, "Test 01 failed in class AddTest")

    def test02_add_same_items(self):
        """ Tests if lists with a few same and different items add correctly"""
        a = LetterManager("abcdef")
        b = LetterManager("abcghi")
        l = [['a'], [2], ['b'], [2], ['c'], [2], ['d'], [1], ['e'], [1], ['f'], [1],
            ['g'], [1], ['h'], [1], ['i'], [1], ['j'], [0], ['k'], [0], ['l'], [0],
            ['m'], [0], ['n'], [0], ['o'], [0], ['p'], [0], ['q'], [0], ['r'], [0],
            ['s'], [0], ['t'], [0], ['u'], [0], ['v'], [0], ['w'], [0], ['x'], [0],
            ['y'], [0], ['z'], [0], ]
        self.assertEqual(a.Add(b).alpha_counter, l, "Test 02 failed in class AddTest")

    def test03_add_punct_spaces_chr(self):
        """ Tests if lists with spaces, punctuation, nonaplha characters add correctly"""
        a = LetterManager(" *@#89034@]@#2''';")
        b = LetterManager("98097(*!)(70-40+")
        l = [['a'], [0], ['b'], [0], ['c'], [0], ['d'], [0], ['e'], [0], ['f'], [0],
            ['g'], [0], ['h'], [0], ['i'], [0], ['j'], [0], ['k'], [0], ['l'], [0],
            ['m'], [0], ['n'], [0], ['o'], [0], ['p'], [0], ['q'], [0], ['r'], [0],
            ['s'], [0], ['t'], [0], ['u'], [0], ['v'], [0], ['w'], [0], ['x'], [0],
            ['y'], [0], ['z'], [0], ]
        self.assertEqual(a.Add(b).alpha_counter, l, "Test 03 failed in class AddTest")

    def test04_add_list_with_mixed_lengths(self):
        """ Tests if lists with completely different letters and sizes add correctly"""
        a = LetterManager("abc")
        b = LetterManager("rtz")
        l = [['a'], [1], ['b'], [1], ['c'], [1], ['d'], [0], ['e'], [0], ['f'], [0],
            ['g'], [0], ['h'], [0], ['i'], [0], ['j'], [0], ['k'], [0], ['l'], [0],
            ['m'], [0], ['n'], [0], ['o'], [0], ['p'], [0], ['q'], [0], ['r'], [1],
            ['s'], [0], ['t'], [1], ['u'], [0], ['v'], [0], ['w'], [0], ['x'], [0],
            ['y'], [0], ['z'], [1], ]
        self.assertEqual(a.Add(b).alpha_counter, l, "Test 04 failed in class AddTest")

    def test05_add_two_empty_lists(self):
        """ Tests if two empty lists add correctly"""
        a = LetterManager("")
        b = LetterManager("")
        l = [['a'], [0], ['b'], [0], ['c'], [0], ['d'], [0], ['e'], [0], ['f'], [0],
            ['g'], [0], ['h'], [0], ['i'], [0], ['j'], [0], ['k'], [0], ['l'], [0],
            ['m'], [0], ['n'], [0], ['o'], [0], ['p'], [0], ['q'], [0], ['r'], [0],
            ['s'], [0], ['t'], [0], ['u'], [0], ['v'], [0], ['w'], [0], ['x'], [0],
            ['y'], [0], ['z'], [0], ]
        self.assertEqual(a.Add(b).alpha_counter, l, "Test 05 failed in class AddTest")


class SubtractTest(unittest.TestCase):

    def test01_subtract_different_items(self):
        """ Tests if lists with different items add correctly"""
        a = LetterManager("abcdef")
        b = LetterManager("ghijkl")
        self.assertEqual(a.Subtract(b), None, "Test 01 failed in class SubtractTest")

    def test02_subtract_same_items(self):
        """ Tests if lists with a few same and different items add correctly"""
        a = LetterManager("abcdef")
        b = LetterManager("abcdef")
        l = [['a'], [0], ['b'], [0], ['c'], [0], ['d'], [0], ['e'], [0], ['f'], [0],
            ['g'], [0], ['h'], [0], ['i'], [0], ['j'], [0], ['k'], [0], ['l'], [0],
            ['m'], [0], ['n'], [0], ['o'], [0], ['p'], [0], ['q'], [0], ['r'], [0],
            ['s'], [0], ['t'], [0], ['u'], [0], ['v'], [0], ['w'], [0], ['x'], [0],
            ['y'], [0], ['z'], [0], ]
        self.assertEqual(a.Subtract(b).alpha_counter, l, "Test 02 failed in class SubtractTest")

    def test03_subtract_punct_spaces_chr(self):
        """ Tests if lists with spaces, punctuation, nonaplha characters add correctly"""
        a = LetterManager(" *@#89034@]@#2''';")
        b = LetterManager("98097(*!)(70-40+")
        l = [['a'], [0], ['b'], [0], ['c'], [0], ['d'], [0], ['e'], [0], ['f'], [0],
            ['g'], [0], ['h'], [0], ['i'], [0], ['j'], [0], ['k'], [0], ['l'], [0],
            ['m'], [0], ['n'], [0], ['o'], [0], ['p'], [0], ['q'], [0], ['r'], [0],
            ['s'], [0], ['t'], [0], ['u'], [0], ['v'], [0], ['w'], [0], ['x'], [0],
            ['y'], [0], ['z'], [0], ]
        self.assertEqual(a.Subtract(b).alpha_counter, l, "Test 03 failed in class SubtractTest")

    def test04_subtract_list_with_mixed_lengths(self):
        """ Tests if lists with completely different letters and sizes add correctly"""
        a = LetterManager("abc")
        b = LetterManager("rtz")
        self.assertEqual(None, a.Subtract(b), "Test 04 failed in class SubtractTest")

    def test05_subtract_two_empty_lists(self):
        """ Tests if two empty lists add correctly"""
        a = LetterManager("")
        b = LetterManager("")
        l = [['a'], [0], ['b'], [0], ['c'], [0], ['d'], [0], ['e'], [0], ['f'], [0],
            ['g'], [0], ['h'], [0], ['i'], [0], ['j'], [0], ['k'], [0], ['l'], [0],
            ['m'], [0], ['n'], [0], ['o'], [0], ['p'], [0], ['q'], [0], ['r'], [0],
            ['s'], [0], ['t'], [0], ['u'], [0], ['v'], [0], ['w'], [0], ['x'], [0],
            ['y'], [0], ['z'], [0], ]
        self.assertEqual(a.Subtract(b).alpha_counter, l, "Test 05 failed in class SubtractTest")

    def test06_subtract_two_similar_lists(self):
        """ Tests if two empty lists add correctly"""
        a = LetterManager("abcdef")
        b = LetterManager("abcdeg")
        self.assertEqual(a.Subtract(b), None, "Test 06 failed in class SubtractTest")


from letter_manager_anagram import *


class AnagramTest(unittest.TestCase):

    def test01_same_words(self):
        """ Tests if two same words are anagrams"""
        a = AnagramChecker()
        self.assertEqual(a.testchecker('hi', 'hi'), "Word 1 & 2 are anagrams.", "Test 01 failed in class AnagramTest")

    def test02_same_word_with_space(self):
        """ Tests if two same words are anagrams (one word with whitespace around it)"""
        a = AnagramChecker()
        self.assertEqual(a.testchecker('hi', ' hi '), "Word 1 & 2 are not anagrams.",
                         "Test 02 failed in class AnagramTest")

    def test03_(self):
        """ Tests if two different words are anagrams"""
        a = AnagramChecker()
        self.assertEqual(a.testchecker('hi', 'bye'), "Word 1 & 2 are not anagrams.",
                         "Test 03 failed in class AnagramTest")

    def test04_empty_words(self):
        """ Tests if two different words are anagrams"""
        a = AnagramChecker()
        self.assertEqual(a.testchecker('', ''), "Word 1 & 2 are not anagrams.",
                         "Test 04 failed in class AnagramTest")

    def test05_mixed_up_words(self):
        """ Tests if two words (same size and letters) are anagrams"""
        a = AnagramChecker()
        self.assertEqual(a.testchecker('racecar', 'carrace'), "Word 1 & 2 are anagrams.",
                         "Test 05 failed in class AnagramTest")

    def test06_mixed_up_words_w_space(self):
        """ Tests if two words (same size and letters) are anagrams"""
        a = AnagramChecker()
        self.assertEqual(a.testchecker('race car', 'carrace'), "Word 1 & 2 are not anagrams.",
                         "Test 06 failed in class AnagramTest")

if __name__ == "__main__":
    unittest.main()

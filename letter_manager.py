class LetterManager:

    def __init__(self, string):
        """(str)
        Construct an inventory (a count) of the alphabetic letters in the
        given string, ignoring the case of letters and ignoring any non-alphabetic characters.
        """
        self.alpha_counter = [['a'], [0], ['b'], [0], ['c'], [0], ['d'], [0], ['e'], [0], ['f'], [0],
                              ['g'], [0], ['h'], [0], ['i'], [0], ['j'], [0], ['k'], [0], ['l'], [0],
                              ['m'], [0], ['n'], [0], ['o'], [0], ['p'], [0], ['q'], [0], ['r'], [0],
                              ['s'], [0], ['t'], [0], ['u'], [0], ['v'], [0], ['w'], [0], ['x'], [0],
                              ['y'], [0], ['z'], [0], ]
        self.count = 0
        string = string.strip().lower()
        for i in string:
            if i.isalpha():
                idx = self.alpha_counter.index([i]) + 1
                self.alpha_counter[idx][0] += 1
                self.count += 1

    def Get(self, letter):
        """(str)
        Returns a count of letter in the inventory.
        """
        alp_list = self.alpha_counter

        try:
            if not isinstance(letter, str) or not letter.isalpha():
                raise InputError(letter)
            if len(letter) != 1:
                raise InputError(letter)
        except (NameError, InputError):
            print("Invalid User Input.")
        else:
            return alp_list[alp_list.index([letter]) + 1][0]

    def Set(self, letter, value):
        """(str, int)
        Sets the count for the given letter to the given value in the inventory.
        """
        try:
            if not (isinstance(letter, str) and isinstance(value, int)):
                raise InputError(letter)
            if not (letter.isalpha() and str(value).isnumeric()):
                raise NameError(value)
            if value < 0:
                raise InputError(value)
        except (InputError, NameError):
            print("Invalid User Input.")
        else:
            idx = self.alpha_counter.index([letter]) + 1
            count_helper = value - self.alpha_counter[idx][0]
            self.count += count_helper
            self.alpha_counter[idx][0] = value

    def Size(self):
        """
        Returns the sum of all of the counts in this inventory.
        """
        return self.count

    def IsEmpty(self):
        """
        Returns true if this inventory is empty (all counts are 0).
        """
        return self.count == 0

    def __str__(self):
        """
        Returns a String representation of the inventory with the letters all in lowercase
        and in sorted order and surrounded by square brackets.
        """
        result = '['
        alp_list = self.alpha_counter
        for i in range(1, 52, 2):
            if alp_list[i][0] > 0:
                result += (alp_list[i][0] * alp_list[i-1][0])

        return result + ']'

    def Add(self, lm):
        """
        Takes another LetterManager, and constructs and returns a new LetterManager object that
        represents the sum of this letter manager and the other given letter manager.
        """
        manager1 = str(self)
        manager2 = str(lm)
        new = LetterManager(manager1 + manager2)
        return new

    def Subtract(self, lm):
        """
        Return a new LetterManager object that represents the result of
        subtracting lm from this manager.
        """
        man1 = list(self.alpha_counter)
        man2 = lm.alpha_counter
        result = ""
        for i in range(0, 52, 2):
            man1[i + 1][0] -= man2[i + 1][0]
            if man1[i + 1][0] < 0:
                return None
            else:
                result += man1[i][0] * man1[i + 1][0]
        return LetterManager(result)

class InputError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


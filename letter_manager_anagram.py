from letter_manager import *


class AnagramChecker:

    def checker(self):
        """
        Returns whether two words are anagrams or not.
        """
        word1 = input("Word 1: ")
        word2 = input("Word 2: ")

        result = -1
        if not (word1.isalpha() and word2.isalpha()):
            result = -1
        elif len(word1) != len(word2):
            result = -1
        elif str(LetterManager(word1)) == str(LetterManager(word2)):
            result = 0

        if result == 0:
            print("Word 1 & 2 are anagrams.")
        else:
            print("Word 1 & 2 are not anagrams.")

    def testchecker(self, word1, word2):
        """
        TEST PURPOSES ONLY: Returns whether two words are anagrams or not.
        """
        result = -1
        if not (word1.isalpha() and word2.isalpha()):
            result = -1
        elif len(word1) != len(word2):
            result = -1
        elif str(LetterManager(word1)) == str(LetterManager(word2)):
            result = 0

        if result == 0:
            return("Word 1 & 2 are anagrams.")
        else:
            return("Word 1 & 2 are not anagrams.")

if __name__ == "__main__":
    m = input('enter 0 to end')
    while m != str(0):
        x = AnagramChecker()
        x.checker()
        m = input('enter 0 to end')

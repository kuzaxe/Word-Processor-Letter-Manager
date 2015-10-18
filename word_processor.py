from stack import *


class WordProcessor:

    def __init__(self):
        self._stack = Stack()
        self._undo = Stack()
        self._redo = Stack()
        self.last_call = ''

    def undo(self):
        """
        Reverses the last action that was made to main _stack if it is valid.
        """
        try:
            if self._undo.size() == 0:
                raise InputError(self._undo.size())
        except InputError:
            print("Error: Cannot call undo.")
        else:
            item = self._undo.pop()
            if item[0] == "add":                                    # If 'add', undo adding an item to the stack
                self._stack.pop()
                self._redo.push(item)
            else:                                                   # Else: undo the delete made; put item back
                self._stack.items.insert(item[2], item[1])
                self._redo.push(item)

    def redo(self):
        """
        Reverses the last step called by the user if it is valid.
        """
        try:
            if self._redo.size() == 0:
                raise InputError(self._redo.size())
        except InputError:
            print("Command Error: Cannot Call 'redo'.")
        else:
            item = self._redo.pop()
            self._undo.push(item)
            if item[0] == "add":                                    # If 'add', re-push the item into the main stack
                self._stack.push(item[1])
            else:                                                   # Else: remove the previous item user deleted.
                idx = item[2]
                self._stack.items.pop(idx)

    def delete(self, line):
        """
        Removes a line (selected by the user) from
        the main _stack if line is valid.
        Line 1 is in index 0, line 2 is in index 1, etc.
        """
        try:
            if self._stack.size() == 0:
                raise InputError(self._stack.size())
            if not int(line):
                raise InputError(line)
            if int(line) > self._stack.size() or 0 >= int(line):
                raise IndexError(self._stack.size())
        except (InputError, ValueError):
            print("Input Error: Cannot Execute Your Command.")
        except IndexError:
            print("Input Error: Index Out of Range.")
        else:
            del_idx = int(line) - 1                                 # Index of the item to delete.
            item = self._stack.items.pop(del_idx)
            self._undo.push(["del", item, del_idx])

    def main(self):
        """ Prompts the user for commands until user enters whitespace.
        """
        line = input("Command?")

        while line != "":
            WordProcessor.commands(self, line)
            line = input("Command?")
        if self.last_call == 'add':
            self._redo = []

    def commands(self, line):
        """ Assesses the command user inputted
        and calls the methods accordingly.
        """
        if line == "d":
            WordProcessor.delete(self, input("Which Line?"))
            print(self._stack.items)
            self.last_call = 'd'
        elif line == "undo":
            WordProcessor.undo(self)
            print(self._stack.items)
            self.last_call = 'undo'
        elif line == "redo":
            WordProcessor.redo(self)
            print(self._stack.items)
            self.last_call = 'redo'
        else:
            self._stack.push(line)
            self._undo.push(['add', line, int(self._stack.size())])
            self._redo = Stack()
            print(self._stack.items)
            self.last_call = 'add'

        print("        undo", self._undo.items)
        print("        redo", self._redo.items)


class InputError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


if __name__ == "__main__":
    x = WordProcessor()
    x.main()

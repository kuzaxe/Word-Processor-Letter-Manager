from stack import *

def swap(s):
    """swap top two items on stack s"""
    if s.size() > 0:
        top_item = s.pop()
        s.items.insert(-1, top_item)

def roll(s, n):
    """
    perform the roll operation on a stack s.
    A roll with integer n causes the nth item from the top to be removed
    and placed on top of the stack.
    """
    if s.size() > 0 and 0 < n <= s.size():
        idx = -n
        nth_item = s.items.pop(idx)
        s.push(nth_item)


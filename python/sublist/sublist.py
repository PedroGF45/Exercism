"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 'is sublist'
SUPERLIST = 'is superlist'
EQUAL = 'is equal'
UNEQUAL = 'is unequal'


def sublist(list_one, list_two):
    
    if list_one == list_two:
        return EQUAL
    
    # check if any sublist of list two is equal to the first list
    if list_one == [] or any(map(lambda x: list_one == list_two[x : x + len(list_one)], range(len(list_two)))):
        return SUBLIST
    
    # check if any sublist of first list is equal to the second list
    if list_two == [] or any(map(lambda x: list_two == list_one[x : x + len(list_two)], range(len(list_one)))):
        return SUPERLIST
    
    return UNEQUAL

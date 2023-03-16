# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):

    # count number of ones, twos, threes, fours, fives and sixes
    if category > 0 and category < 7:
        if category in dice:
            return category * dice.count(category)
        else:
            return 0

    # if the category is a full house
    if category == 7:
        if len(set(dice)) == 2 and (dice.count(dice[0]) == 3 or dice.count(dice[0]) == 2):
            return sum(dice)
        else:
            return 0
    
    # if the category is four of a kind
    if category == 8:
        if len(set(dice)) <= 2 and dice.count(dice[0]) >= 4:
            return 4 * dice[0]
        elif len(set(dice)) <= 2 and dice.count(dice[1]) >= 4: 
            return 4 * dice[1]
        else:
            return 0
    
    # if the category is little straight or big straight
    straight = [1, 2, 3, 4, 5, 6]
    if category == 9:
        if all(map(lambda x: x in dice, straight[:-1])):
            return 30
        else:
            return 0
    if category == 10:
        if all(map(lambda x: x in dice, straight[1:])):
            return 30
        else:
            return 0
    
    # category is choice
    if category == 11:
        return sum(dice)
    
    # category is yacht
    if category == 0:
        if dice.count(dice[0]) == 5:
            return 50
        return 0

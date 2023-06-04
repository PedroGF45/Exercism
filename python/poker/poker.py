STRAIGHT_FLUSH = 8
FOUR_OF_A_KIND = 7 
FULL_HOUSE = 6
FLUSH = 5
STRAIGHT = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0

def best_hands(hands):
    
    for hand in hands:
        print(check_hands(hand.replace('K', '13').replace('Q', '12').replace('J', '11').replace('A', '14').split()))


def check_hands(hand):

    print(hand)
    # straight flush
    naipe_sf = all(map(lambda x: hand[x][-1] == hand[x+1][-1] , range(1, len(hand)-1, 1)))
    numbers_sf = all(map(lambda x: (int(hand[x+1][:-1]) - int(hand[x][:-1]) == 1) , range(0, len(hand)-1, 1)))

    if naipe_sf and numbers_sf:
        return STRAIGHT_FLUSH
    

    # four of a kind
    if (hand.count(hand[0]) == 4 or hand.count(hand[2]) == 4):
        return FOUR_OF_A_KIND
    
    # full house
    numbers_fh = sorted(hand)[:5]
    if ((numbers_fh.count(numbers_fh[0]) == 3 and numbers_fh.count(numbers_fh[3]) == 2) or 
        (numbers_fh.count(numbers_fh[0]) == 2 and numbers_fh.count(numbers_fh[2]) == 3)):
        return FULL_HOUSE
    
    # flush
    if naipe_sf:
        return FLUSH
    
    # straight
    if numbers_sf:
        return STRAIGHT
    
    # three of a kind
    if ((numbers_fh.count(numbers_fh[0]) == 3) or numbers_fh.count(numbers_fh[2]) == 3):
        return THREE_OF_A_KIND
    
    # two pair
    if (numbers_fh.count(numbers_fh[1]) == 2 and numbers_fh.count(numbers_fh[3]) == 2):
        return TWO_PAIR
    
    # one pair
    if (numbers_fh.count(numbers_fh[1]) == 2 or numbers_fh.count(numbers_fh[3]) == 2):
        return TWO_PAIR
    
    return HIGH_CARD
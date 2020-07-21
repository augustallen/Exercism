import numpy as np

# Score categories.
def yacht(dice):
    score = all(elem == dice[0] for elem in dice)
    if score:
        return 50
    else:
        return 0

def ones(dice):
    score = 0
    for die in dice:
        if die==1:
            score += die
    return score

def twos(dice):
    score = 0
    for die in dice:
        if die==2:
            score += die
    return score

def threes(dice):
    score = 0
    for die in dice:
        if die==3:
            score += die
    return score

def fours(dice):
    score = 0
    for die in dice:
        if die==4:
            score += die
    return score

def fives(dice):
    score = 0
    for die in dice:
        if die==5:
            score += die
    return score

def sixes(dice):
    score = 0
    for die in dice:
        if die==6:
            score += die
    return score

def full_house(dice):
    values, counts = np.unique(dice, return_counts=True)
    if len(counts)==2 and 2 in counts and 3 in counts:
        return sum(dice)
    return 0

def four_of_a_kind(dice):
    values, counts = np.unique(dice, return_counts=True)
    values, counts = list(values), list(counts)
    if 4 in counts:
        return 4*values[counts.index(4)]
    if 5 in counts:
        return 4*values[counts.index(5)]
    return 0

def little_straight(dice):
    values = list(np.unique(dice))
    if values == [1,2,3,4,5]:
        return 30
    return 0

def big_straight(dice):
    values = list(np.unique(dice))
    if values == [2,3,4,5,6]:
        return 30
    return 0

# Change the values as you see fit.
YACHT = yacht
ONES = ones
TWOS = twos
THREES = threes
FOURS = fours
FIVES = fives
SIXES = sixes
FULL_HOUSE = full_house
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT = little_straight
BIG_STRAIGHT = big_straight
CHOICE = lambda d: sum(d)

def score(dice, category):
    return category(dice) 
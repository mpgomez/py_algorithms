from collections import Counter

def score(dice):
    dice_counter = Counter([10 if x == 1 else x for x in dice])
    score = 0
    for i in dice_counter.keys():
        if dice_counter.get(i, 0) >= 3:
            score += i * 100
            dice_counter[i]-=3

    score += (dice_counter.get(10, 0)*10 + dice_counter.get(5, 0)*5) * 10
    return score
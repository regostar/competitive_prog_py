# https://codeforces.com/problemset/problem/2014/A

# Not all people having 0 gold will get gold
# only if robin has >=1 gold he will give them
# prev houe should be rich

# O(n) 
# start with first person
# if he is rich, ie gold[i] >= k robin will take all gold[i]
# maintain gold stock held by robin G
# find next  person, if he has == 0 gold, then give them 1 gold
# subtract gold stock G -1
# if  not repeat
# 
# can we optimize this?
# we need to only find the no of people who will get gold from robin
# we need to find no of 0s which gold stock >= k before them

from typing import List

def find_no_of_gold_receivers(n: int, k: int, gold: List[int])->int:
    """
    Will compute and return no of people who will receive gold
    k -> threshold
    n -> no of people
    gold -> array containing gold held by each person
    """
    gold_stock = 0
    # robin starts out with 0 stock of gold
    no_of_recipients = 0

    for each in gold:
        if each >= k:
            # robin steals
            gold_stock += each
        elif each == 0 and gold_stock > 0:
            gold_stock -= 1
            no_of_recipients += 1
            # robin will give gold

    return no_of_recipients





if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n, k = list(map(int, input().split()))
        gold = list(map(int, input().split()))

        print(find_no_of_gold_receivers(n, k, gold))
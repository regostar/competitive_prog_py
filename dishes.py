# https://codeforces.com/contest/1313/problem/A
# A. Fast Food Restaurant
# Regostar Codes!

def display_max_visitors(dishes: list):
    # We know the max visitors having unique dishes combo cannot be more than 7, so we make the truth table
    dishes.sort(reverse=True)
    # unique dishes combo arranged in an order to maximize the number of visitors:-
    truth_table = [
        [1,0,0],
        [0,1,0],
        [0,0,1],
        [1,1,0],
        [1,0,1],
        [0,1,1],
        [1,1,1],
    ]
    no_of_visitors = 0
    for combo in truth_table:
        dishes = [d - c for d, c in zip(dishes, combo)]
        if -1 in dishes: # this combo cannot be made
            dishes = [d + c for d, c in zip(dishes, combo)] # reverse change
        else:
            no_of_visitors += 1
    print(no_of_visitors)


def main():
    trials = int(input())
    for _ in range(trials):
        dishes = list(map(int, input().split()))
        display_max_visitors(dishes)


if __name__ == '__main__':
    main()




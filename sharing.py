import math
test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    b = 1
    a = n - 1
    if not a > b:
        print('0')
    else:
        counter = math.floor((n-1)/2)
        print(counter)
    
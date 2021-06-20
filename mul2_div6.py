
t = int(input())

for _ in range(t):
    n = int(input())
    ctr = 0
    while n % 6 == 0:
        n = n/6
        ctr += 1
    while n % 3 == 0:
        n = n/3
        ctr += 2
    if n != 1:
        print("-1")
    else:
        print((ctr))
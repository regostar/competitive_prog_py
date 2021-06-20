from math import ceil

t = int(input())
for _ in range(t):
    row, col = map(int,input().split())
    print(ceil((row * col) / 2))
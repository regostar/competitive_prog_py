from math import floor
def find_req_rem(x, y, n):
    max_factor = floor(n/x)
    while (max_factor*x)+y > n:
        max_factor -= 1
    return (max_factor*x)+y



t = int(input())
for _ in range(t):
    a, b, n = map(int,input().split())
    no_of_ops = find_req_rem(a, b, n)
    print(no_of_ops)
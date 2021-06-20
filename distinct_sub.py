t = int(input())

for _ in range(t):
    n, a, b = list(map(int,input().split()))
    print(''.join(chr(i%b+97)for i in range(n)))
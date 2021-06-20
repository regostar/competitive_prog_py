t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    print('W'+'\n'.join(['B'*m]*n)[1:])
    
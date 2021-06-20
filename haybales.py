t = int(input())

for i in range(t):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    ptr = 1
    while d and ptr < len(a):
        print(d)
        val = ptr * a[ptr]
        if val <= d:
            d = d - val
            a[0] += a[ptr]
            a[ptr] = 0
        else:
            ctr = a[ptr]
            while ctr > 0:
                ctr -= 1
                if ptr * ctr <= d:
                    d = d - (ptr * ctr)
                    a[0] += ctr
                    a[ptr] -= ctr
        ptr += 1
    print(a[0])
        


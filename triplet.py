t = int(input())
for _ in range(t):
    xyz = list(map(int, input().split()))
    mx = max(xyz)
    if xyz.count(mx) < 2:
        print("NO")
    else:
        print("YES")
        other = xyz[0]
        for ele in xyz:
            if ele != mx:
                other = ele
        print(mx, 1, other)
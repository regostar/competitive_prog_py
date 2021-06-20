t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    ordered = []
    for ele in lst:
        if ele not in ordered:
            ordered.append(ele)
    print(' '.join(map(str, ordered)))
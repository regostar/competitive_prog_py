
t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    i = 0
    found = False
    for index in range(1, n-1):
        if lst[index] > lst[index-1] and lst[index+1] < lst[index]:
            found = True
            break
    if found:
        print("YES")
        print(index, index+1, index+2)
    else:
        print("NO")






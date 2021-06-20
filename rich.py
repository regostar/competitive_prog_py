I= lambda : list(map(int,input().split()))
 
for _ in range(int(input())):
    n,x = I()
    w=sorted(I())
    answer=n
    s=sum(w)
    for i in range(n):
        if x<=s/answer:
            break
        answer -= 1
        s -= w[i]
    print(answer)
 
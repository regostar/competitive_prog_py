n = int(input())
b = list(map(int, input().split(' ')))

x = [0]
a = []

a.append(b[0])
x.append(a[0])

i = 1
while i < n:
    a.append(b[i]+x[i])
    if a[i] > x[i]:
        x.append(a[i])
    else:
        x.append(x[i])
    i += 1
    
str_a = [str(ele) for ele in a]
print(' '.join(str_a))
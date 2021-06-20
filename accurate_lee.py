t = int(input())

for _ in range(t):
    n = int(input())
    bstr = input()
    one = bstr.find('1')
    zero = bstr.rfind('0')
    # 01
    if one > zero:
        print(bstr)
    else:
        print(bstr[0:one]+bstr[zero:n])

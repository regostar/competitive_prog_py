
def coins_distributed(a, b, c, n) -> str:
    """
    """
    sum = a + b + c + n
    if sum % 3 == 0:
        if max(a,b,c) <= sum/3:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"

t = int(input())
for i in range(t):
    a,b,c,n = [int(x) for x in input().split(' ')]
    print(coins_distributed(a,b,c,n))

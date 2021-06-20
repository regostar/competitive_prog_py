# def find_min_op(a: int, b: int, n: int):
#     """
#     """
#     count = 0
#     while a <= n and b <= n:
#         if count %2 ==0:
#             a += b
#         else:
#             b += a
#         count += 1
#     return count

def find_min_op(a: int, b: int, n: int):
    """
    """
    count = 0
    while b <= n:
        a, b = max(a, b), b+a
        count += 1
    return count

t = int(input())
for _ in range(t):
    a, b, n = map(int,input().split())
    no_of_ops = find_min_op(a, b, n)
    print(no_of_ops)
def min_square_area(x: int, y: int):
    """
    """
    smallest_side = min(x, y)
    longest_side = max(x, y)
    square_side = 2*smallest_side
    if square_side < longest_side:
        square_side = longest_side
    return square_side * square_side

t = int(input())
for _ in range(t):
    a, b = map(int,input().split())
    sq_area  = min_square_area(a, b)
    print(sq_area)
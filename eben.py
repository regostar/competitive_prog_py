
def get_eben(n: list):
    if sum(n) % 2 == 0:
        return int("".join(map(str, n)))
    num = n
    s = sum(num)
    while s % 2 != 0:
        s 
        

        


def main():
    t = int(input())
    for _ in range(t):
        length = int(input())
        n = map(int, input().split())
        print(get_eben(n))




if __name__=='__main__':
    main()

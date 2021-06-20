# CopyCopyCopyCopyCopy
# https://codeforces.com/contest/1325/problem/B


def longest_subseq(seq, n):
    print(len(set(seq)))

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        seq = list(map(int, input().split(' ')))
        longest_subseq(seq, n)

if __name__ == "__main__":
    main()
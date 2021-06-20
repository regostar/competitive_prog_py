def main():
    n = int(input())
    robo_coder = list(map(int, input().split()))
    bionic_silver = list(map(int, input().split()))
    # print(robo_coder)
    # print(bionic_silver)
    print(min_val(robo_coder, bionic_silver, n))

def min_val(robo_coder, bionic_silver, n):
    rc = 0
    bs = 0
    min_val = 0
    i = 0
    while i in range(n):
        if robo_coder[i] and not bionic_silver[i]:
            rc += 1
        if not robo_coder[i] and bionic_silver[i]:
            bs += 1
        i += 1
    # print("rc ", rc)
    # print("bs ", bs)
    if not rc:
        return -1

    while min_val * rc <= bs:
        min_val += 1
    return min_val

if __name__ == '__main__':
    main()


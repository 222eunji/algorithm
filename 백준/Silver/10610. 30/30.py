import sys
input = sys.stdin.readline

N = [int(c) for c in input().strip()]

if (0 in N) and (sum(N) % 3 == 0) :
    N.sort(reverse=True)
    print(''.join(map(str, N)))

else:
    print(-1)
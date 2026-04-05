import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = list(int(input()) for _ in range(N))
cnt = 0

for i in range(len(coins)-1, -1, -1):
    if K >= coins[i]:
        cnt += K // coins[i]
        K = K % coins[i]
        if K == 0:
            break

print(cnt)
import sys
input = sys.stdin.readline


n, goal = map(int,input().split())
coin_type = list(map(int, [input() for _ in range(n)]))

cnt = 0
for i in range(n-1, -1, -1):
  if goal >= coin_type[i]:
    cnt += goal // coin_type[i]
    goal %= coin_type[i]

print(cnt)
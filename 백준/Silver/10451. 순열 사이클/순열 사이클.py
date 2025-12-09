import sys
input = sys.stdin.readline

def solve():
  n = int(input())
  perm = [0] + list(map(int, input().split()))

  visited = [False] * (n+1)
  cycle_count = 0

  for i in range(1, n+1):
    if not visited[i]:
      # 새로운 사이클 시작
      cycle_count += 1

      current = i
      while not visited[current]:
        visited[current] = True
        current = perm[current]

  print(cycle_count)

T = int(input())
for _ in range(T):
  solve()
  
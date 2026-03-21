import sys
input = sys.stdin.readline

def dfs():
  n = int(input())
  perm = [0] + list(map(int,input().split()))
  cycle_cnt = 0
  visited = [False] * (n+1)
  
  for i in range(1, n+1):
    while not visited[i]:
      cycle_cnt += 1
      current = i

      while not visited[current]:
        visited[current] = True
        current = perm[current]

  print(cycle_cnt)

T = int(input())
for _ in range(T):
  dfs()
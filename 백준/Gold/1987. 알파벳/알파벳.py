import sys;
input = sys.stdin.readline

r, c = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(r)]

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
max_v = -1

def dfs(i, j, mask, cnt):
    global max_v
    max_v = max(max_v, cnt)

    for di, dj in d:
        ni, nj = i + di, j + dj
        if 0 <= ni < r and 0 <= nj < c:
            nxt = ord(grid[ni][nj]) - ord('A')
            if not (mask & (1 << nxt)):
                dfs(ni, nj, mask | (1 << nxt), cnt+1)

start_mask = 1 << (ord(grid[0][0]) - ord('A'))
dfs(0,0, start_mask, 1)
print(max_v)
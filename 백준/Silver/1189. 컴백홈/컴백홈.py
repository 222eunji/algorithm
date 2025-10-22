import sys
input = sys.stdin.readline

# 최소거리는 아니어도 되는건가? 그럼 dfs 아니야?
# 한번 갔던 길만 간다 (되돌아가지 않음)
# 값이 T면 못감
# 출발 인덱스:(R-1, 0) / 도착 인덱스: (0, C-1)
R, C, K = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
result = 0
visited = [[False] * C for _ in range(R)]


def dfs(r, c, cnt):
    global result
    if r == 0 and c == C-1 and cnt == K:
        result += 1
        return

    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == False and grid[nr][nc] != 'T':
            visited[nr][nc] = True
            dfs(nr, nc, cnt+1)
            visited[nr][nc] = False


visited[R-1][0] = True
dfs(R-1, 0, 1)  # 출발점에서 시작
print(result)
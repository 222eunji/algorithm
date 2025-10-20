import sys;
input = sys.stdin.readline
from collections import deque

monkeys = [(1,0), (-1,0), (0,1), (0,-1)]
horse = [(-2,-1), (-2,1),(-1,2),(1,2),(2,-1),(2,1),(-1,-2),(1,-2)]
def bfs():
    visited = [[[False] * (K+1) for _ in range(W)] for _ in range(H)]
    # r, c, 남은k, 이동 횟수 넣기
    q = deque([(0,0,0,0)])
    visited[0][0][0] = True

    while q:
        r, c, used_k, dist = q.popleft()

        if r == H-1 and c == W-1:
            return dist

        # 원숭이 이동
        for dr, dc in monkeys:
            nr, nc = r+dr, c+dc
            if 0 <= nr < H and 0 <= nc < W: # 인덱스 체크
                if visited[nr][nc][used_k] == False and grid[nr][nc] == 0: # 방문 안했고, 장애물 없을 때
                    visited[nr][nc][used_k] = True
                    q.append((nr, nc, used_k, dist+1))

        # 말처럼 이동
        if used_k < K:
            for dr, dc in horse:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W:
                    if visited[nr][nc][used_k+1] == False and grid[nr][nc] == 0:  # 방문 안했고, 장애물 없을 때
                        visited[nr][nc][used_k+1] = True
                        q.append((nr, nc, used_k+1, dist+1))

    return -1

# K: 말처럼 뛰는 횟수
# W,H: 격자판의 가로, 세로 길이
# H줄에 걸쳐 맵 주어짐, 0은 평지 1은 장애물
# 말은 장애물을 뛰어넘을 수 있음

K = int(input())
W, H = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

print(bfs())
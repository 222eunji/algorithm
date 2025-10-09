import sys;
input = sys.stdin.readline
from collections import deque
from itertools import combinations
import copy


# 입력 받기
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]


# 바이러스 출발 위치, 빈공간 찾고 기존 벽 개수 카운트하기
def find_123(grid):
    empty = []
    origin_wall = 0
    virus_pos = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                empty.append((i, j))
            elif grid[i][j] == 1:
                origin_wall += 1
            elif grid[i][j] == 2:
                virus_pos.append((i, j))
    return empty, origin_wall, virus_pos

# 바이러스 퍼트리기
d = [(1,0), (-1,0),(0,1),(0,-1)]
def virus(virus_pos, virus_map):
    q = deque(virus_pos)
    visited = [[False] * M for _ in range(N)]

    while q:
        i, j = q.popleft()
        visited[i][j] = True

        for di, dj in d:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == False:
                if virus_map[ni][nj] == 0:
                    virus_map[ni][nj] = 2
                    q.append((ni, nj))
                visited[ni][nj] = True

# 바이러스 개수 찾기
def count_virus(virus_map):
    global min_virus
    cnt_virus = 0
    for i in range(N):
        for j in range(M):
            if virus_map[i][j] == 2:
                cnt_virus += 1
                if min_virus <= cnt_virus:
                    return  # 바이러스개수가 많아지면 종료하기
    min_virus = min(min_virus, cnt_virus)


min_virus = float('inf')
empty, origin_wall, virus_pos = find_123(grid)
for walls in combinations(empty, 3):
    temp_grid = copy.deepcopy(grid)
    for i, j in walls:
        temp_grid[i][j] = 1 # 벽 세우기
    virus(virus_pos, temp_grid) # 바이러스 퍼트리기
    count_virus(temp_grid)

print(N*M-origin_wall-3-min_virus)
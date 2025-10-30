import sys
input = sys.stdin.readline
from collections import deque

# 같은 색 뿌요가 4개이상 상하좌우로 연결되어있으면, 같은색 뿌요들이 한번에 없어짐 => 1연쇄 시작
# 아래로 떨어지고 다시 같은 색의 뿌요들이 4개 이상 모이게 되면 또 터짐
# 터진 후 뿌요들이 내려오고, 이것을 반복할 때 마다 1연쇄씩 늘어남




R, C= 12, 6

# bfs로 뿌요 4개이상 확인하는 함수
#  - 4개 이상인 거 체크
#  - .으로 바꾸기
#  - 여러개의 뿌요 모두 동시에터져야함
grid = [list(input().strip()) for _ in range(R)]

d = [(1,0), (-1,0), (0,1), (0,-1)]
def bfs(sr, sc, color):
    q = deque([(sr, sc)])
    visited = [[False] * C for _ in range(R)]
    color_pos = []

    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == color and visited[nr][nc] == False:
                q.append((nr, nc))
                visited[nr][nc] = True
                color_pos.append((nr,nc))

    # bfs 탐색 다하고 난 뒤, 4개 이상이 연결되면 .으로 바꾸기
    if len(color_pos) >= 4:
        for r, c in color_pos:
            grid[r][c] = '.'
        return True     # 4개 이상 이면 True 반환
    return False    # 아니면 False 반환


# 아래로 떨어지는 함수
def fall():
    for c in range(C):
        stack = deque([])
        for r in range(R-1, -1, -1):
            if grid[r][c] != '.':
                stack.append(grid[r][c])
        # 위에서부터 다시 채우기
        for r in range(R-1, -1, -1):
            if stack:
                grid[r][c] = stack.popleft()
            else:
                grid[r][c] = '.'


# 위 두 함수 한바퀴 돌 때마다 연쇄 +1
def puyo_puyo():
    chain = 0
    while True:
        visited = [[False] * C for _ in range(R)]
        boom = False    # 이번 턴에 터졌는지 여부 확인

        for r in range(R):
            for c in range(C):
                if grid[r][c] != '.':
                    if bfs(r, c, grid[r][c]):
                        boom = True

        if boom:
            fall()
            chain += 1
        else:
            break

    print(chain)


puyo_puyo()

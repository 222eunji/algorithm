import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 치킨집 찾기, 집 위치 찾기
chicken = []
house = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 2:
            chicken.append((i, j))
        elif grid[i][j] == 1:
            house.append((i, j))

# 집에서 치킨집까지의 거리
dist = [[0]*len(chicken) for _ in range(len(house))]

for i, (hx, hy) in enumerate(house):
    for j, (cx, cy) in enumerate(chicken):
        dist[i][j] = abs(cx-hx) + abs(cy-hy)


# 치킨집 M개 선택하기
result = float('inf')
selected_chicken = []
def comb(start, cnt):
    global result
    if cnt == M:
        temp_dist = 0
        for h in range(len(house)):
            temp_dist += min(dist[h][c] for c in selected_chicken)
        result = min(result, temp_dist)
        return

    for i in range(start, len(chicken)):
        selected_chicken.append(i)
        comb(i+1, cnt+1)
        selected_chicken.pop()

comb(0, 0)
print(result)

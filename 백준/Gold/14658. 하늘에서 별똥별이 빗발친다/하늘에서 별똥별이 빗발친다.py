import sys
input = sys.stdin.readline


N, M, L, K = map(int, input().split())
stars = []
for _ in range(K):
    x, y = map(int, input().split())
    stars.append((x, y))

max_defend = 0
for i in range(K):
    for j in range(K):
        r1, c1 = stars[i][0], stars[j][1]
        count = 0

        for r, c in stars:
            if r1 <= r <= r1 + L and c1 <= c <= c1 + L:
                count += 1
        max_defend = max(max_defend, count)

print(K- max_defend)

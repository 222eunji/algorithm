import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# memo[r][i] = (최댓값, 최솟값)
memo = [[(0, 0) for _ in range(3)] for _ in range(N)]

# 첫 행 초기화
for i in range(3):
    memo[0][i] = (arr[0][i], arr[0][i])

# DP 진행
for r in range(1, N):
    for i in range(3):
        candidates = []
        for d in (-1, 0, 1):
            c = i + d
            if 0 <= c < 3:
                candidates.append(memo[r-1][c])
        
        # 이전 칸들의 최댓값 중 최대, 최솟값 중 최소
        max_val = max(val[0] for val in candidates) + arr[r][i]
        min_val = min(val[1] for val in candidates) + arr[r][i]
        
        memo[r][i] = (max_val, min_val)

# 마지막 행에서 답 찾기
result_max = max(memo[N-1][i][0] for i in range(3))
result_min = min(memo[N-1][i][1] for i in range(3))

print(result_max, result_min)
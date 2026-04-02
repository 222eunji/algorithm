import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = []
i, j = 0, 0
while i < N and j < M:
    if A[i] <= B[j]:
        result.append(A[i])
        i += 1
    else:
        result.append(B[j])
        j += 1

# 남은 원소 추가
result += A[i:]
result += B[j:]

print(*result)
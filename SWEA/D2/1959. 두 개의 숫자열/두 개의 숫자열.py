
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N < M:
        A, B = B, A     # 언제나 A가 더 긴 리스트로 설정
        N, M = M, N

    max_v = 0
    for start in range(N-M+1):
        sum_v = 0
        for i in range(M):
            sum_v += A[start + i]*B[i]
        max_v = max(max_v, sum_v)

    print(f'#{tc} {max_v}')
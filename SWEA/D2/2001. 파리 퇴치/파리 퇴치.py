
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 1. prefix 배열 초기화
    prefix = [[0] * (N+1) for _ in range(N+1)]

    # 2. prefix 채우기
    for i in range(1, N+1):
        for j in range(1, N+1):
            prefix[i][j] = (grid[i-1][j-1]
                            + prefix[i-1][j]
                            + prefix[i][j-1]
                            - prefix[i-1][j-1])

    # 3. 파리채 잡기
    max_catch = 0
    for i in range(M, N+1):
        for j in range(M, N+1):
            total = (prefix[i][j]
                     - prefix[i-M][j]
                     - prefix[i][j-M]
                     + prefix[i-M][j-M])
            max_catch = max(total, max_catch)

    print(f'#{tc} {max_catch}')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 완전탐색
    max_catch = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            catch = 0
            for r_idx in range(M):
                for c_idx in range(M):
                    catch+=grid[i+r_idx][j+c_idx]

            if max_catch < catch:
                max_catch = catch

    print(f'#{tc} {max_catch}')
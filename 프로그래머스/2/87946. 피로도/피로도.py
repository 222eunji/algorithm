def solution(k, dungeons):
    max_cnt = 0
    visited = [False] * len(dungeons)
    
    def recur(health, cnt):
        nonlocal max_cnt

        max_cnt = max(max_cnt, cnt)
        for idx in range(len(dungeons)):
            # 현재 피로도가 최소 필요 피로도 이상일 때만 탐험 가능
            if (visited[idx] == False) and (health >= dungeons[idx][0]) and (health - dungeons[idx][1]) >= 0:
                visited[idx] = True
                recur(health-dungeons[idx][1], cnt+1)
                visited[idx] = False
                
    recur(k, 0)
    return max_cnt




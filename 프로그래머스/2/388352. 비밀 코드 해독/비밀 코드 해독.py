def solution(n, q, ans):
    answer = 0
    code = []
    def comb (start, picked):
        nonlocal answer
        if picked == 5:
            flag = True
            for i in range(len(q)):
                cnt = 0
                for e in code:
                    if e in q[i]:
                        cnt += 1
                if cnt != ans[i]:
                    flag = False
                    break
            if flag:
                answer += 1
            return
        for i in range(start, n+1):
            code.append(i)
            comb(i+1, picked+1)
            code.pop()
        
    # n개 조합 후 q를 돌면서 백트래킹
    comb(1,0)
    return answer
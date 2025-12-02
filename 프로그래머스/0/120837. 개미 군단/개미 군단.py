def solution(hp):
    answer = 0
    # 장군개미 개수
    answer += (hp // 5)
    hp %= 5
    
    # 병정개미 개수
    answer += (hp // 3)    
    hp %= 3

    # 일개미 개수
    answer += hp
    
    return answer
def solution(num, k):
    num = str(num)
    k = str(k)
    answer = num.find(k)
    if answer == -1:
        return answer
    else:        
        return answer + 1
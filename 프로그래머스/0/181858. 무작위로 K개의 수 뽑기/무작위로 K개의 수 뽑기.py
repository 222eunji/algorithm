def solution(arr, k):
    answer = []
    for n in arr:
        if n not in answer:
            answer.append(n)
        
        if len(answer) == k:
            break
    
    if len(answer) < k:
        plus = [-1] * (k - len(answer))
        answer += plus
        
    return answer
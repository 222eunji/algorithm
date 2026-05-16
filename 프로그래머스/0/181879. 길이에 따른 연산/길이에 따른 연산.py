def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        answer = 1
        for n in num_list:
            answer *= n
        return answer
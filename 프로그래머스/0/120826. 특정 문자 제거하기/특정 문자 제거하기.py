def solution(my_string, letter):
    answer = ''
    for ch in my_string:
        if ch == letter:
            continue
        answer += ch
    return answer
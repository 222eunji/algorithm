def solution(myString):
    answer = ''
    for c in myString:
        if ord(c) < 97:
            answer += chr(ord(c) + 32)
        else:
            answer += c
    return answer
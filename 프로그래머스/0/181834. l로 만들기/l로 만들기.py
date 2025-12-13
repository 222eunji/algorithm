def solution(myString):
    answer = []
    for ch in myString:
        if ord(ch) < ord('l'):
            answer.append('l')
        else:
            answer.append(ch)
    
    return ''.join(answer)
def solution(myString):
    answer = ''
    for c in myString:
        if c == 'a':
            answer += 'A'
        else:
            if 65 < ord(c) < ord('a'):
                answer += chr(ord(c) + 32)
            else:
                answer += c            
    return answer

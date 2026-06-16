def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        new = []
        if i % 2:
            for c in strArr[i]:
                if ord(c) < 97:
                    new.append(c)
                else:
                    new.append(chr(ord(c)-32))
        else:
            for c in strArr[i]:
                if ord(c) < 97:
                    new.append(chr(ord(c)+32))            
                else:
                    new.append(c)            
        answer.append(''.join(new))
    return answer
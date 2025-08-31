def solution(sentence):
    set = {'{':'}', '(':')'}
    stack = []
    for c in sentence:
        if c in '{(':
            stack.append(c)
        elif c in '})':
            if stack:   # stack에 값이 있다면
                if c == set[stack.pop()]:
                    continue
                else:
                    return 0
            else:       # stack에 값이 없다면
                return 0
    if stack:
        return 0
    else:
        return 1


T = int(input())
for tc in range(1, T+1):
    sentence = input()
    print(f'#{tc} {solution(sentence)}')

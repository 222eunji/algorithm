def solution(s):
    cnt = [0] * 26
    for ch in s:
        cnt[ord(ch) - 97] += 1
    ans = ''
    str = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(26):
        if cnt[i] == 1:
            ans += str[i]    
    return ans
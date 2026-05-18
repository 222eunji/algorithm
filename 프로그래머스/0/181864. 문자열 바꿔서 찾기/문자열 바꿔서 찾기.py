def solution(myString, pat):
    pat_r = ""
    for c in pat:
        if c == "A":
            pat_r += "B"
        else:
            pat_r += "A"
            
    if pat_r in myString:
        return 1
    return 0
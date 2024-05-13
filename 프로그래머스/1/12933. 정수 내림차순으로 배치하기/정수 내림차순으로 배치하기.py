def solution(n):
    strlist = list(str(n))
    strlist = sorted(strlist, key = lambda x : -int(x))
    size = len(strlist) - 1
    answer = 0
    for s in strlist:
        if size == 0:
            answer += int(s)
        else:
            answer += int(s) * (10 ** size)
        size -= 1
    return answer
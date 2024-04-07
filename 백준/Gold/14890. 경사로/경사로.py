import sys
input = sys.stdin.readline
import copy

N, L = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]

load = {
    1 : [1,0],
    2 : [0,1],
    -1: [-1,0],
    -2: [0,-1]
}

def checkSlide(x,y,loc):
    global lines
    if lines[x][y]:
        return False
    cnt = 1
    ansLi = [(x,y)]
    h = maps[x][y]
    for _ in range(L-1):
        x += load[loc][0]
        y += load[loc][1]
        if (0 <= x < N) and (0 <= y < N) and h == maps[x][y] and not lines[x][y]:
            cnt += 1
            ansLi.append((x,y))
        else:
            break
    if cnt == L:
        for a,b in ansLi:
            lines[a][b] = True
        return True
    return False

def checkLine(x,y,loc):
    global lines
    lines = [[False] * N for _ in range(N)]
    for _ in range(N-1):
        a, b, h = x, y, maps[x][y]
        x += load[loc][0]
        y += load[loc][1]
        if h == maps[x][y]:
            continue
        elif h - maps[x][y] == 1:
            if checkSlide(x,y,loc):
                continue
            else:
                return False
        elif h - maps[x][y] == -1:
            if checkSlide(a,b,-loc):
                continue
            else:
                return False
        else:
            return False
    return True


answer = 0
for i in range(N):
    if checkLine(i,0,2):
        answer += 1
    if checkLine(0,i,1):
        answer += 1
print(answer)
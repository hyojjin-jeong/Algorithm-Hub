import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
import copy


maps = []
for _ in range(4):
    l = list(map(int,input().split()))
    line = []
    for i in range(0,8,2):
        line.append([l[i],l[i+1]])
    maps.append(line)
moving = {
    1: [-1,0],
    2: [-1,-1],
    3: [0,-1],
    4: [1,-1],
    5: [1,0],
    6: [1,1],
    7: [0,1],
    8: [-1,1]
}

def findFish(num,maps):
    li = []
    for i in range(4):
        for j in range(4):
            if maps[i][j][0] == num:
                li.append(i)
                li.append(j)
                return li
            
def fishMove(maps):
    mmaps = copy.deepcopy(maps)
    for i in range(1,17):
        ab = findFish(i,mmaps)
        if not ab:
            continue
        a, b = ab[0], ab[1]
        loc = mmaps[a][b][1]
        for _ in range(8):
            na, nb = a + moving[loc][0], b + moving[loc][1]
            if (0 <= na < 4) and (0 <= nb < 4) and mmaps[na][nb][0] != 20:
                mmaps[a][b][1] = loc
                mmaps[na][nb], mmaps[a][b] = mmaps[a][b], mmaps[na][nb]
                break
            loc += 1
            if loc == 9:
                loc = 1
    return mmaps

def recycle(x,y,fish,maps):
    global answer
    X, Y = x, y
    moveMap = fishMove(maps)
    moveable = []
    sharkMovnum = moveMap[x][y][1]
    for _ in range(4):
        x += moving[sharkMovnum][0]
        y += moving[sharkMovnum][1]
        if (0 <= x < 4) and (0 <= y < 4) and moveMap[x][y][0] != 0:
            moveable.append((x,y))
    if moveable:
        for a, b in moveable:
            fvalue = moveMap[a][b][0]
            moveMap[a][b][0] = 20
            moveMap[X][Y][0] = 0
            recycle(a,b,fish+fvalue,moveMap)
            moveMap[a][b][0] = fvalue
            moveMap[X][Y][0] = 20
    else:
        answer.append(fish)
        return

f = maps[0][0][0]
maps[0][0][0] = 20
answer = []
recycle(0,0,f,maps)
print(max(answer))
import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
start = int(N/2)
now = [start, start]
moving = {
    "l": [0,-1],
    "r": [0,1],
    "u": [-1,0],
    "d": [1,0]
}
loop = 1
answer = 0
location = {
    "l": {
        1: [(-1,1),(1,1)],
        2: [(-2,0),(2,0)],
        5: [(0,-2)],
        7: [(-1,0),(1,0)],
        10: [(-1,-1),(1,-1)]
    },
    "d": {
        1: [(-1,-1),(-1,1)],
        2: [(0,-2),(0,2)],
        5: [(2,0)],
        7: [(0,-1),(0,1)],
        10: [(1,-1),(1,1)]
    },
    "r": {
        1: [(-1,-1),(1,-1)],
        2: [(-2,0),(2,0)],
        5: [(0,2)],
        7: [(-1,0),(1,0)],
        10: [(-1,1),(1,1)]
    },
    "u": {
        1: [(1,-1),(1,1)],
        2: [(0,-2),(0,2)],
        5: [(-2,0)],
        7: [(0,-1),(0,1)],
        10: [(-1,-1),(-1,1)]
    }
}
alpha = {
    "l": [0,-1],
    "d": [1,0],
    "r": [0,1],
    "u": [-1,0]
}

def persand(sand):
    one = int(sand*0.01)
    two = int(sand*0.02)
    five = int(sand*0.05)
    seven = int(sand*0.07)
    ten = int(sand*0.1)
    d = {
        1: one,
        2: two,
        5: five,
        7: seven,
        10: ten
    }
    return d

def move(x,y,b):
    global answer
    sand = A[x][y]
    per = persand(sand)
    loc = location[b]
    for key, value in loc.items():
        for dx,dy in value:
            nx, ny = x + dx, y + dy
            if (0 <= nx < N) and (0 <= ny < N):
                sand -= per[key]
                A[nx][ny] += per[key]
            else:
                sand -= per[key]
                answer += per[key]
    nx = x + alpha[b][0]
    ny = y + alpha[b][1]
    if (0 <= nx < N) and (0 <= ny < N):
        A[nx][ny] += sand
    else:
        answer += sand
    A[x][y] = 0

cnt = 0
while True:
    if loop % 2 == 1:
        for _ in range(loop):
            now[0] += moving["l"][0]
            now[1] += moving["l"][1]
            if (0 <= now[0] < N) and (0 <= now[1] < N):
                move(now[0],now[1],"l")
            else:
                cnt = 1
                break
        if cnt == 1:
            break
        for _ in range(loop):
            now[0] += moving["d"][0]
            now[1] += moving["d"][1]
            if (0 <= now[0] < N) and (0 <= now[1] < N):
                move(now[0],now[1],"d")
            else:
                cnt = 1
                break
        if cnt == 1:
            break
        loop += 1
    else:
        for _ in range(loop):
            now[0] += moving["r"][0]
            now[1] += moving["r"][1]
            if (0 <= now[0] < N) and (0 <= now[1] < N):
                move(now[0],now[1],"r")
            else:
                cnt = 1
                break
        if cnt == 1:
            break
        for _ in range(loop):
            now[0] += moving["u"][0]
            now[1] += moving["u"][1]
            if (0 <= now[0] < N) and (0 <= now[1] < N):
                move(now[0],now[1],"u")
            else:
                cnt = 1
                break
        if cnt == 1:
            break
        loop += 1
print(answer)
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
r, c, d = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
loc = {
    0: [-1,0],
    1: [0,1],
    2: [1,0],
    3: [0,-1]
}

def cleancnt(x,y):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < M) and maps[nx][ny] == 0:
            cnt += 1
    return cnt

answer = 0
while True:
    if maps[r][c] == 0:
        maps[r][c] = 2
        answer += 1
    cnt = cleancnt(r,c)
    if cnt == 0:
        r -= loc[d][0]
        c -= loc[d][1]
        if maps[r][c] == 1:
            break
        else:
            continue
    else:
        d -= 1
        if d == -1:
            d = 3
        nr = r + loc[d][0]
        nc = c + loc[d][1]
        if maps[nr][nc] == 0:
            r, c = nr, nc
            continue
        else:
            continue
print(answer)
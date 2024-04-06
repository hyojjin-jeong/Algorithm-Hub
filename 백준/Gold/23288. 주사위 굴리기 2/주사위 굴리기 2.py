import sys
input = sys.stdin.readline
from collections import deque  #큐 사용

N, M, K = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
dice = {
    "now": 1,
    "u": 2,
    "r": 3,
}
loc = {
    "l": ["u","d"],
    "r": ["d","u"],
    "u": ["r","l"],
    "d": ["l","r"]
}
mapLoc = {
    "l": [0,-1],
    "r": [0,1],
    "u": [-1,0],
    "d": [1,0]
}
sw = {
    "l": "r",
    "r": "l",
    "u": "d",
    "d": "u"
}
answer = 0
moving = "r"
x, y = 0, 0
def move(moving):
    now, u, r = 0, 0, 0
    if moving == "l":
        now = dice["r"]
        u = dice["u"]
        r = 7 - dice["now"]
    elif moving == "r":
        now = 7 - dice["r"]
        u = dice["u"]
        r = dice["now"]
    elif moving == "u":
        now = 7 - dice["u"]
        u = dice["now"]
        r = dice["r"]
    elif moving == "d":
        now = dice["u"]
        u = 7 - dice["now"]
        r = dice["r"]
    dice["now"] = now
    dice["u"] = u
    dice["r"] = r

def bfs(i,j):
    q = deque()
    visited = [[False] * M for _ in range(N)]
    visited[i][j] = True
    q.append((i,j))
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N) and (0 <= ny < M) and not visited[nx][ny] and maps[nx][ny] == maps[x][y]:
                visited[nx][ny] = True
                cnt += 1
                q.append((nx,ny))
    return cnt


for _ in range(K):
    nx = x + mapLoc[moving][0]
    ny = y + mapLoc[moving][1]
    if (nx < 0 or nx >= N) or (ny < 0 or ny >= M):
        moving = sw[moving]
        nx = x + mapLoc[moving][0]
        ny = y + mapLoc[moving][1]
    move(moving)
    x, y = nx, ny
    B = maps[x][y]
    C = bfs(x,y)
    answer += B * C
    A = 7 - dice["now"]
    if A > B:
        moving = loc[moving][0]
    elif A < B:
        moving = loc[moving][1]
print(answer)  
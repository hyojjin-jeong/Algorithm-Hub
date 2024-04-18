import sys
input = sys.stdin.readline
import copy
from collections import deque  #큐 사용

N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def check(i,j):
    cnt = 0
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if (0 <= ni < N) and (0 <= nj < M) and board[ni][nj] == 0:
            cnt += 1
    return cnt
def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if (0 <= nx < N) and (0 <= ny < M) and not visited[nx][ny] and board[nx][ny] != 0:
                visited[nx][ny] = True
                q.append((nx,ny))
loop = 0
while True:
    icecnt = 0
    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and not visited[i][j]:
                bfs(i,j)
                icecnt += 1
    if icecnt > 1:
        if loop == 0:
            print(0)
            break
        print(loop)
        break
    elif icecnt == 0:
        print(0)
        break

    newb = copy.deepcopy(board)
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                cnt = check(i,j)
                newice = newb[i][j] - cnt
                if newice < 0:
                    newice = 0
                newb[i][j] = newice

    board = newb
    loop += 1
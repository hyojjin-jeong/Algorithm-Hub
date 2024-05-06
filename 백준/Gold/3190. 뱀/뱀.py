import sys
input = sys.stdin.readline
from collections import deque  #큐 사용

N = int(input())
K = int(input())
board = [[0] * (N+1) for _ in range(N+1)]
for _ in range(K):
    x, y = map(int,input().split())
    board[x][y] = 1
L = int(input())
changes = []
for _ in range(L):
    c = input().split()
    changes.append((int(c[0]), c[1]))

snakes = [(1,1)]
loc = {0: [-1,0], 1: [0,1], 2: [1,0], 3: [0,-1]}
visited = [[False] * (N+1) for _ in range(N+1)]
visited[1][1] = True
now = 1
next = changes.pop(0)
cnt = 1
q = deque()
q.append((1,1))
while q:
    x, y = q.popleft()
    nx = x + loc[now][0]
    ny = y + loc[now][1]
    if (1 <= nx <= N) and (1 <= ny <= N) and not visited[nx][ny]:
        visited[nx][ny] = True
        snakes.append((nx,ny))
        q.append((nx,ny))
        if board[nx][ny] == 0:
            tail = snakes.pop(0)
            visited[tail[0]][tail[1]] = False
        else:
            board[nx][ny] = 0
        if cnt == next[0]:
            if next[1] == "L":
                now -= 1
                if now == -1:
                    now = 3
            else:
                now += 1
                if now == 4:
                    now = 0
            if changes:
                next = changes.pop(0)
        cnt += 1
print(cnt)
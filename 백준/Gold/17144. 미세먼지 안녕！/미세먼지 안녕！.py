import sys
input = sys.stdin.readline

R, C, T = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(R)]
air = [
    [[-1,0],[0,1],[1,0],[0,-1]],
    [[1,0],[0,1],[-1,0],[0,-1]]]

def monji(x,y):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    total = A[x][y]
    m = int(total/ 5)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < R) and (0 <= ny < C) and A[nx][ny] != -1:
            deepA[nx][ny] += m
            deepA[x][y] -= m

for _ in range(T):
    deepA = [[0] * C for _ in range(R)]
    a = []
    for i in range(R):
        for j in range(C):
            if A[i][j] > 0:
                monji(i,j)
            elif A[i][j] == -1:
                a.append((i,j))
    for i in range(R):
        for j in range(C):
            if A[i][j] != -1:
                A[i][j] += deepA[i][j]
    c = 0
    for i, j in a:
        I = i
        cnt = 0
        while cnt < 4:
            ni = i + air[c][cnt][0]
            nj = j + air[c][cnt][1]
            if c == 0:
                if (0 <= ni <= I) and (0 <= nj < C):
                    if A[i][j] == -1:
                        A[ni][nj] = 0
                    elif A[ni][nj] == -1:
                        break
                    else:
                        A[i][j], A[ni][nj] = A[ni][nj], A[i][j]
                    i, j = ni, nj
                else:
                    cnt += 1
            else:
                if (I <= ni < R) and (0 <= nj < C):
                    if A[i][j] == -1:
                        A[ni][nj] = 0
                    elif A[ni][nj] == -1:
                        break
                    else:
                        A[i][j], A[ni][nj] = A[ni][nj], A[i][j]
                    i, j = ni, nj
                else:
                    cnt += 1
        c += 1
answer = 0
for i in A:
    answer += sum(i)
print(answer+2)
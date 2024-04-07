import sys
input = sys.stdin.readline

N = int(input())
A = [[0] * (N+1)] + [[0] + list(map(int,input().split())) for _ in range(N)]

def find5(x,d1,d2,reg):
    for i in range(x+1,x+d1+d2):
        cnt = 0
        for j in range(1,N+1):
            if reg[i][j] == 0:
                cnt += 1
                if cnt == 2:
                    break
            else:
                if cnt == 1:
                    reg[i][j] = 0

def divReg(d1,d2,x,y):
    for i in range(d1+1):
        reg[x+i][y-i] = 0
        reg[x+d2+i][y+d2-i] = 0
    for i in range(d2+1):
        reg[x+i][y+i] = 0
        reg[x+d1+i][y-d1+i] = 0
    find5(x,d1,d2,reg)
    for i in range(1,N+1):
        for j in range(1,N+1):
            if reg[i][j] != 0:
                if (1 <= i < x + d1) and (1 <= j <= y):
                    reg[i][j] = 1
                elif (1 <= i <= x + d2) and (y < j <= N):
                    reg[i][j] = 2
                elif (x + d1 <= i <= N) and (1 <= j < y - d1 + d2):
                    reg[i][j] = 3
                elif (x + d2 < i <= N) and (y - d1 + d2 <= j <= N):
                    reg[i][j] = 4
                else:
                    reg[i][j] = 0

def people(reg):
    p = [0,0,0,0,0]
    for i in range(1,N+1):
        for j in range(1,N+1):
            p[reg[i][j]] += A[i][j]
    return max(p) - min(p)

answer = float("inf")
for d1 in range(1,N):
    for d2 in range(1,N):
        for x in range(1, N-d1-d2):
            for y in range(2+d1,N-d2):
                reg = [[5] * (N+1) for _ in range(N+1)]
                divReg(d1,d2,x,y)
                answer = min(answer, people(reg))
print(answer)
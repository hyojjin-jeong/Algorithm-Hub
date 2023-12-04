import sys
input = sys.stdin.readline #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque #큐 사용

N, M = map(int, input().split())
boards = [input() for _ in range(N)]

ans = []

for a in range(N-7):
  for b in range(M-7):
    W = 0
    B = 0
    for i in range(a, a+8):
      for j in range(b, b+8):
        if (i+j)%2 == 0:
          if boards[i][j] != 'W':
            W += 1
          else:
            B += 1
        else:
          if boards[i][j] != "B":
            W += 1
          else:
            B += 1
    ans.append(min(W,B))
print(min(ans))
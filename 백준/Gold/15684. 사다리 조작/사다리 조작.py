import sys
input = sys.stdin.readline

N, M, H = map(int,input().split())
line = [[0 for _ in range(N+1)] for _ in range(H+1)]
for _ in range(M):
  a, b = map(int,input().split())
  line[a][b] = b+1
  line[a][b+1] = b

def check():
  for i in range(1,N+1):
    now = i
    for j in range(1,H+1):
      if line[j][now] != 0:
        now = line[j][now]
    if now != i:
      return False
  return True

def make_line(cnt):
  global answer
  if check():
    answer = min(answer, cnt)
    return
  elif cnt >= 3:
    return
  for i in range(1,H+1):
    for j in range(1,N):
      if line[i][j] == 0 and line[i][j+1] == 0:
        line[i][j], line[i][j+1] = j+1, j
        make_line(cnt+1)
        line[i][j], line[i][j+1] = 0, 0
  return
answer = 5
make_line(0)
if answer == 5:
  print(-1)
else:
  print(answer)
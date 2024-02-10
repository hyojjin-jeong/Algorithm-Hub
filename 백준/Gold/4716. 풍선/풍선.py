import sys
input = sys.stdin.readline

while True:
  N, A, B = map(int,input().split())
  if N == 0 and A == 0 and B == 0:
    break
  teams = [list(map(int,input().split())) for _ in range(N)]
  teams = sorted(teams, key = lambda x : -abs(x[1]-x[2]))
  answer = 0
  for i in range(N):
    if teams[i][1] < teams[i][2]:
      if teams[i][0] > A:
        answer += A * teams[i][1]
        teams[i][0] -= A
        A = 0
        B -= teams[i][0]
        answer += teams[i][2] * teams[i][0]
      else:
        A -= teams[i][0]
        answer += teams[i][1] * teams[i][0]
    elif teams[i][1] > teams[i][2]:
      if teams[i][0] > B:
        answer += B * teams[i][2]
        teams[i][0] -= B
        B = 0
        A -= teams[i][0]
        answer += teams[i][0] * teams[i][1]
      else:
        B -= teams[i][0]
        answer += teams[i][0] * teams[i][2]
    else:
      if A <= B:
        B -= teams[i][0]
        answer += teams[i][0] * teams[i][2]
      else:
        A -= teams[i][0]
        answer += teams[i][0] * teams[i][1]
  print(answer)
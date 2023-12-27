import sys
input = sys.stdin.readline  #필수로 해놓기

T = int(input())
for _ in range(T):
  scores = input().rstrip()
  sum = 0
  cnt = 0
  for i in range(len(scores)):
    if scores[i] == "O":
      cnt += 1
      sum += cnt
    elif scores[i] == "X":
      cnt = 0
  print(sum)
import sys
input = sys.stdin.readline  #필수로 해놓기

M = int(input())
S = []
for _ in range(M):
  Input = input()
  if " " in Input:
    word, num = Input.split()
  else:
    word, num = Input.rstrip(), 0
  if word == "add" and int(num) not in S:
    S.append(int(num))
  elif word == "remove" and int(num) in S:
    S.remove(int(num))
  elif word == "check":
    if int(num) in S:
      print(1)
    else:
      print(0)
  elif word == "toggle":
    if int(num) in S:
      S.remove(int(num))
    else:
      S.append(int(num))
  elif word == "all":
    S = [i for i in range(1,21)]
  elif word == "empty":
    S = []
    

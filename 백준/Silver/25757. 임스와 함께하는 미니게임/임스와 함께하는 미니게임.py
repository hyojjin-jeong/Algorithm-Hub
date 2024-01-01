import sys
input = sys.stdin.readline  #필수로 해놓기

N, kind = input().rstrip().split()
N = int(N)

peoples = set(list(input().rstrip() for _ in range(N)))

if kind == "Y":
  print(len(peoples))
elif kind == "F":
  print(len(peoples)//2)
elif kind == "O":
  print(len(peoples)//3)
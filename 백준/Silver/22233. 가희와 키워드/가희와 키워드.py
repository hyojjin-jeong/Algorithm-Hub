import sys
input = sys.stdin.readline  #필수로 해놓기

N, M = map(int,input().split())
keywords = set()
for _ in range(N):
  keywords.add(input().rstrip())
for _ in range(M):
  write = input().rstrip().split(',')
  for i in set(write):
    if i in keywords:
      keywords.remove(i)
  print(len(keywords))

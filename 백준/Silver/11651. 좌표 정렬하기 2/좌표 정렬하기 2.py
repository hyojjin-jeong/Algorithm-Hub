import sys
input = sys.stdin.readline

N = int(input())
li = [list(map(int,input().split())) for _ in range(N)]
li = sorted(li, key=lambda x : (x[1], x[0]))
for l in li:
  print(*l)
import sys
input = sys.stdin.readline  #필수로 해놓기

N, M, L, K = map(int,input().split())
list = [list(map(int,input().split())) for _ in range(K)]
answer = 0
for x,y in list:
  for xx,yy in list:
    num = 0
    for xxx,yyy in list:
      if x <= xxx <= x + L and yy <= yyy <= yy + L:
        num += 1
    answer = max(answer, num)
print(K - answer)
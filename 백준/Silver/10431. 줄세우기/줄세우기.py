import sys
input = sys.stdin.readline  #필수로 해놓기

P = int(input())
for _ in range(P):
  heights = list(map(int,input().split()))
  i = heights.pop(0)
  cnt = 0
  hsort = [heights.pop(0)]
  for height in heights:
    lenth = len(hsort)
    for j in range(lenth):
      if height < hsort[j]:
        hsort.insert(j,height)
        cnt += lenth-j
        break
    if lenth == len(hsort):
      hsort.append(height)
  print(i,cnt)
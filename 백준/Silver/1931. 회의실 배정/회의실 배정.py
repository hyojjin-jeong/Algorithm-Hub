import sys
input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

N = int(input())
times = []
for _ in range(N):
  times.append(list(map(int,input().split())))
times = sorted(times, key = lambda x : (x[1],x[0]))
end = 0
cnt = 0
for x,y in times:
  if end <= x:
    cnt += 1
    end = y
print(cnt)
      

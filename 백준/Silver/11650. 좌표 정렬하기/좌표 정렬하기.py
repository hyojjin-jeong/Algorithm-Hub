import sys
input = sys.stdin.readline #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque #큐 사용

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = sorted(arr, key = lambda x : (x[0], x[1]))

for i in range(N):
  print(ans[i][0],ans[i][1])
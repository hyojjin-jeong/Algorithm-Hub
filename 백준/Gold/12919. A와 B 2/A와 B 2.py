import sys
input = sys.stdin.readline  #필수로 해놓기
sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요

S = input().rstrip()
T = input().rstrip()

ans = 0

def alphaMatch(T):
  global ans
  if S == T:
    ans = 1
    return 0
  elif len(T) == 1:
    return 0
  reverseT = T[::-1]
  if T[-1] == "A":
    alphaMatch(T[:-1])
  if reverseT[-1] == "B":
    alphaMatch(reverseT[:-1])
  return 0
alphaMatch(T)
print(ans)
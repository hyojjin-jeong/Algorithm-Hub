import sys
input = sys.stdin.readline  #필수로 해놓기

S = input().rstrip()
num = int(input())
print(S[num-1])
import sys
input = sys.stdin.readline  #필수로 해놓기

N = int(input())
list = list(map(int,input().split()))

print(min(list), max(list))

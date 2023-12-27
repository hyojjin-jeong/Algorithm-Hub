import sys
input = sys.stdin.readline  #필수로 해놓기

N = int(input())
list = [input().rstrip() for _ in range(N)]
list = set(list)
list = sorted(list, key = lambda x : (len(x),x))
for i in range(len(list)):
    print(list[i])
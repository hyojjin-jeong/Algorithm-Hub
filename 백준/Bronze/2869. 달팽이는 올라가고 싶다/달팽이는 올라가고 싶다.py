import sys
import math
input = sys.stdin.readline

A, B, V = map(int,input().split())
s = math.ceil((V - A) / (A - B))
print(s + 1)
T = int(input())
for t in range(T):
    bus = [0 for _ in range(5001)]
    N = int(input())
    for _ in range(N):
        A, B = map(int,input().split())
        for i in range(A, B+1):
            bus[i] += 1
    P = int(input())
    print(f'#{t + 1}', end=" ")
    for _ in range(P):
        C = int(input())
        print(f'{bus[C]}', end=" ")
    print()
def main():
    T = int(input())
    for t in range(T):
        A, B, C = map(int,input().split())
        answer = 0
        if B < 2 or C < 3:
            answer = -1
        else:
            if B >= C:
                answer += B - (C - 1)
                B = C - 1
            if A >= B:
                answer += A - (B - 1)
                A = B - 1
        print(f'#{t+1} {answer}')


if __name__ == "__main__":
    main()
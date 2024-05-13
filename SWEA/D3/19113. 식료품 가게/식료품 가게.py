def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        prices = list(map(int,input().split()))
        answer = []
        for _ in range(N):
            p = prices.pop(0)
            answer.append(p)
            realP = p / 0.75
            prices.remove(int(realP))
        print(f'#{t+1} ', end="")
        for a in answer:
            print(a, end=" ")
        print()


if __name__ == "__main__":
    main()
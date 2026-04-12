def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def main():
    print("\n4. 1부터 n까지의 합")
    n = int(input("n 입력: "))
    print("합계:", sum_n(n))

if __name__ == "__main__":
    main()
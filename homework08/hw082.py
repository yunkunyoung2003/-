def gugudan(dan):
    for i in range(1, 10):
        print(dan, "x", i, "=", dan * i)


def main():
    print("구구단")
    dan=int(input("숫자입력: "))
    gugudan(dan)

if __name__ == "__main__":
    main()

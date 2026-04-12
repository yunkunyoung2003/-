def c2f(t_c):
    t_f = (9 / 5) * t_c + 32
    return t_f

def main():
    print("\n3. 섭씨 -> 화씨")
    temp_c = float(input("섭씨 온도 입력: "))
    print("화씨 온도:", c2f(temp_c))

if __name__ == "__main__":
    main()

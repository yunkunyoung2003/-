def main() :
    calories = {"한라봉": 50, "딸기": 34, "바나나": 77}
    total_cal = 0
    fruit_eat_list = ["한라봉","딸기","바나나"]
    for item in fruit_eat_list:
        fruit_eat = int(input(f"{item}을 먹은 양을 입력하세요=>"))
        total_cal += calories[item]* fruit_eat
    print(f"총 칼로리는{total_cal :.2f}입니다.")
if __name__ == "__main__":
    main()

temp_c = input("온도를 입력하시오. ") # 키보드에서 입력값 받기
temp_c = int(temp_c) # 문자를 숫자로 변환
temp_f = temp_c * 1.8 + 32
print(f"{temp_c}C => {temp_f}F")


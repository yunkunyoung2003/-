print("1부터 4까지 기능을 선택해") #기능선택
print("1. 화씨 -> 섭씨")
print("2. 섭씨 -> 화씨")
print("3. 피트(ft) -> cm")
print("4. cm -> 피트(ft)")

선택 = int(input("번호를 입력하세요: ")) #기능선택

값 = float(input("값을 입력하세요: ")) #선택한 기능에 값을 입력

# 변환 처리
if 선택 == 1:
    result = (값 - 32) * 5 / 9 #화씨를 섭씨로 변환하는 공식
    print(f"섭씨: {result:.1f}")

elif 선택 == 2:
    result = 값 * 9 / 5 + 32 #섭씨를 화씨로 변환하는 공식
    print(f"화씨: {result:.1f}")

elif 선택 == 3:
    result = 값 * 30.48 #피트를 cm로 변환하는 공식
    print(f"cm: {result:.1f}")

elif 선택 == 4:
    result = 값 / 30.48 #cm를 피트로 변환하는 공식
    print(f"피트(ft): {result:.1f}")

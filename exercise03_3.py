import math
몸무게 = int(input("몸무게를 입력해. ")) # 키보드에서 입력값 받기
키 = int(input("키를 입력해. "))
키=키/100 #cm를 m로 변환
몸무게 = int(몸무게) # 문자를 숫자로 변환
BMI=몸무게/math.pow(키,2)  #BMI = "몸무게"/"키"^2
print(BMI)



import math
x = int(input("점 x 입력해"))
y = int(input("점 y 입력해"))

if x > 0 and y > 0: #x점이 양수 y점도 양수이면 점(x,y)는 제 1사분면
    print(f"입력한 좌표({x}, {y})는 제 1사분면입니다.")
elif x < 0 and y > 0: #x점이 음수 y점이 양수이면 점(x,y)는 제 2사분면
    print(f"입력한 좌표({x}, {y})는 제 2사분면입니다.")
elif x < 0 and y < 0: #x점이 음수 y점도 음수이면 점(x,y)는 제 3사분면
    print(f"입력한 좌표({x}, {y})는 제 3사분면입니다.")
elif x > 0 and y < 0: #x점이 양수 y점이 음수이면 점(x,y)는 제 4사분면
    print(f"입력한 좌표({x}, {y})는 제 4사분면입니다.")

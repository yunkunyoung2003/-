import math
x1 = int(input("점 x1 입력해"))
y1 = int(input("점 y1 입력해"))
x2 = int(input("점 x2 입력해"))
y2 = int(input("점 y2 입력해"))

거리 = math.sqrt((x2-x1)**2 + (y2-y1)**2) #두 점 사이의 거리를 구하는 공식
#math.sqrt는 제곱근을 나타내는 math 함수  #**2는 2제곱이라는 뜻
print(거리)
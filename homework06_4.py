import math

print("각도  sin값   cos값   tan값")

for 각도 in range(0, 91, 1):
    rad = math.radians(각도)

    sin_v = math.sin(rad)
    cos_v = math.cos(rad)
    tan_v = math.tan(rad)

    print(각도, round(sin_v,3), round(cos_v,3), round(tan_v,3))
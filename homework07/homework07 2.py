mart = {
      "우유": 2800,
      "계란": 300,
      "빵": 1200,
      "물": 1700
 }

cart = ["우유", "우유", "계란", "계란", "계란"]

total = 0

for item in cart:
    total += mart[item]

print("총 구매 금액은 {}원 입니다.".format(total))

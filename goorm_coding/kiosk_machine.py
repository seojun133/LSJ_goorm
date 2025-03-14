menu = [
    ("Pizza", 12000),
    ("Burger", 8000),
    ("Pasta", 15000),
    ("Sushi", 20000),
    ("Salad", 6000)
]
order_list = {}

# 메뉴 출력
print("\n메뉴판\n" + "="*20)
for food, price in menu:
    print(f"{food}: {price}원")
print("="*20)

# 주문 입력
while True:
    food_name = input("주문할 음식 (done 입력 시 종료): ")
    if food_name.lower() == "done":
        break
    for item, price in menu:
        if item == food_name:
            quantity = int(input(f"{food_name} 몇 개? "))
            if food_name in order_list:
                order_list[food_name] += quantity
            else:
                order_list[food_name] = quantity
            break
    else:
        print("없는 메뉴입니다. 다시 입력해주세요.")

print("\n주문 내역\n" + "="*20)
total_price = 0
for food_name, quantity in order_list.items():
    food_price = next(price for item, price in menu if item == food_name) * quantity
    total_price += food_price
    print(f"{food_name} x {quantity}개 - {food_price}원")
print("="*20)
print(f"총 가격: {total_price}원")


products = ["노트북 1200000", "키보드 50000", "마우스 30000", "모니터 250000"]


product_info = [
    {"name": name, "price": int(price), "discount_price": int(price) * 0.9}
    for name, price in (p.split() for p in products)
]

print("상품 정보:")
for product in product_info:
    print(f"{product['name']} - 원가: {product['price']}원, 할인가: {int(product['discount_price'])}원")
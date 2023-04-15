products = {}

while True:
    data = input("Enter product and price: ")
    parts = data.split()

    if len(parts) != 2:
        break

    name, price = parts
    price = int(price)

    if name in products:
        products[name] += price
    else:
        products[name] = price

print("Product\tTotal Price")
for name, price in products.items():
    print(f"{name}\t{price}")

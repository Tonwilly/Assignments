def calculate_discount(price, discount_percent):
    if(discount_percent >= 20):
        price = price - (price * discount_percent/100)
        print(f"Price after discount: {price}") 
    else:
        print(f"Original price: {price}")

print("Enter a price and discount of an item")

item_price = float(input("Price: "))
item_discount = float(input("Discount in %: "))

calculate_discount(item_price, item_discount)

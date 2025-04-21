def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Example with values filled in
original_price = 100.0
discount_percent = 25.0

final_price = calculate_discount(original_price, discount_percent)

if discount_percent >= 20:
    print(f"Discount applied. Final price: ${final_price:.2f}")
else:
    print(f"No discount applied. Price remains: ${final_price:.2f}")
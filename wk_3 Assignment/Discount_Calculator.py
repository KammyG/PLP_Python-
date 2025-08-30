def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # apply discount only if 20% or higher
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price  # no discount applied

original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount)

# Print result
if discount >= 20:
    print(f"Final price after {discount}% discount: {final_price}")
else:
    print(f"No discount applied. Final price: {final_price}")

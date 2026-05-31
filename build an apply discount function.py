def apply_discount(price, discount):
    # 1. Check if price is a number (int or float)
    if not isinstance(price, (int, float)):
        return "The price should be a number."
    
    # 2. Check if discount is a number (int or float)
    if not isinstance(discount, (int, float)):
        return "The discount should be a number."
    
    # 3. Check if price is greater than 0
    if price<= 0:
        return "The price should be greater than 0."
    
    # 4. Check if discount is between 0 and 100 inclusive
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100."
    
    # 5. Calculate and return the final price
    final_price = price * (1 - discount / 100)
    return final_price
apply_discount(price,discount)

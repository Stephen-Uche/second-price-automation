def calculate_discount_price(discount: float, sub_total: float):
    return sub_total - (sub_total*(discount/100))

def calculate_tax(tax_percentile: float, sub_total: float)-> float:
    total = sub_total + (sub_total*(tax_percentile/100))
    return round(total, 4)

def calculate_items_total_pricing(items: dict)-> float:
    total = 0
    for item in items:
        qty = item["quantity"]
        price = item["price"]
        sub_total: float = price*qty
        total += sub_total
    return total
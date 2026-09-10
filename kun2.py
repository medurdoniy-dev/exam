def find_top_seller(products : dict , sales: dict) :
    top_product = max(products, key=lambda product: products[product] * sales[product])
    return top_product

# test:
print(find_top_seller(
    {"Olma": 5000, "Banan": 8000, "Uzum": 7000}, 
    {"Olma": 10, "Banan": 5, "Uzum": 8}
))

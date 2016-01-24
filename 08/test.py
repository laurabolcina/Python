from cash_register import product_prices

def testing_product_prices():
    assert product_prices("bread") == 2.5
    return "testing_product_prices() passed successfully"

print testing_product_prices()
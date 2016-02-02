# coding=utf-8
__author__ = "Laura Bolčina"

products = {"bananas": 1.4, "apples": 1.7, "bread": 2.5, "milk": 0.7}

def product_prices(product):
    price = products[product]
    return price

def main():
    print product_prices("bananas")

if __name__ == "__main__":
    main()
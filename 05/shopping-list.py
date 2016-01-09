# coding=utf-8
__author__ = "Laura Bolčina"

shopping_list = []

adding = True
while adding:
    shopping = raw_input("Do you want to anything your shopping list? (Y/N) ")
    if shopping in "Yy":
        item = raw_input("Enter the item: ")
        shopping_list.append(item)
    else:
        adding = False

print shopping_list
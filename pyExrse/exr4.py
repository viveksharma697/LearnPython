# 8. Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.

# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

def discount(x, y):
    z = float(x * (100 - y)/100)
    return z

a = int(input("Original Price : "))
b = int(input("Discount to be given in % age : "))
print("Price after discount : ", discount(a, b) )
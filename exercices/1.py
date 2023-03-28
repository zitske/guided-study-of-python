# Create a function that takes two integers and returns the product, but
# if the product is greater than 1000, returns the sum.

def product_or_sum(x, y):
    product = x * y
    if product > 1000:
        return x + y
    else:
        return product
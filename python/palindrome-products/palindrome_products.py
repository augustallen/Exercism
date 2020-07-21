def largest(min_factor, max_factor):
    if min_factor>max_factor:
        raise ValueError("min_factor must be smaller than max_factor.")
    pal = palindrome_products(min_factor,max_factor)
    if pal:
        value = max(pal)
        factors = pal[value]
    else:
        value = None
        factors = []
    return value, factors

def smallest(min_factor, max_factor):
    if min_factor>max_factor:
        raise ValueError("min_factor must be smaller than max_factor.")
    pal = palindrome_products(min_factor,max_factor)
    if pal:
        value = min(pal)
        factors = pal[value]
    else:
        value = None
        factors = []
    return value, factors   

def palindrome_products(min_factor, max_factor):
    palindrome_products = {}
    x = min_factor
    while x<=max_factor:
        y = min_factor
        while y<=max_factor:
            if str(x*y) == str(x*y)[::-1]: 
                if (x*y) not in palindrome_products:
                    palindrome_products.update({x*y : [[x,y]]})
                if (x*y) in palindrome_products and [x,y] not in palindrome_products[x*y] and [y,x] not in palindrome_products[x*y]:
                    palindrome_products[x*y].append([x,y])
            y+=1
        x+=1
    return palindrome_products
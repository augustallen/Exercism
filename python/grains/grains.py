def square(number):
    if number>0 and number<65:
        return 2**(number-1)
    else:
        raise ValueError("Number must be between 1 and 64.")

def total():
    total=0
    i = 1
    while i<65:
        total+=square(i)
        i+=1
        print(total)
    return total
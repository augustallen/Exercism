def is_armstrong_number(number):
    total = 0
    for digit in str(number):
        total += int(digit)**len(str(number))
        print(total)
    return total==number
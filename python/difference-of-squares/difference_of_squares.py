def square_of_sum(number):
    total = 0
    for digit in range(1,number+1):
        total += int(digit)
    return total**2

def sum_of_squares(number):
    total = 0
    for digit in range(1,number+1):
        total += int(digit)**2
    return total

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
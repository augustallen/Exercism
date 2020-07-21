import math

def score(x, y):
    distance = math.sqrt(x**2 + y**2)
    if distance > 10:
        points = 0
    elif distance > 5:
        points = 1
    elif distance > 1:
        points = 5
    elif distance >= 0:
        points = 10
    return points
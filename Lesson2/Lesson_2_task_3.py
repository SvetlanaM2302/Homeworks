import math

def square(side):
    square = side * side
    side = math.ceil(side)
    return square
 
print(square(6))
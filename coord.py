import math

a1 = float(input())
b1 = float(input())
c1 = float(input())

a2 = float(input())
b2 = float(input())
c2 = float(input())

distance = math.sqrt((a2 - a1)**2 + (b2 - b1)**2 + (c2 - c1)**2)

print(distance)
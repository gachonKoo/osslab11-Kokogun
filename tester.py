import geo.utils as utils
__all__ = ['pythagoras' , 'circle']
import math

def pythagoras(a, b):
  c = math.sqrt(a**2 + b**2)
  return c

def circle(r):
  area = math.pi * r**2
  return area

# calculate the length of hypotenuse(c) a = 3 & b = 4
a, b = 3, 4
c = utils.pythagoras(a, b)
print('c =', c)

# calculate the area of circle with radius r = 10
r = 10
area = utils.circle(r)
print('area =', area)

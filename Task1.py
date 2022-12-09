import sys
import math
from decimal import *


okr = int(input('Введите количество знаков после запятой'))
def bellard(n):
    pi = Decimal(0)
    k = 0
    while k < n:
      pi += (Decimal(-1)**k/(1024**k))*( Decimal(256)/(10*k+1) + Decimal(1)/(10*k+9) - Decimal(64)/(10*k+3) - Decimal(32)/(4*k+1) - Decimal(4)/(10*k+5) - Decimal(4)/(10*k+7) - Decimal(1)/(4*k+3))
      k += 1
    pi = pi * 1/(2**6)
    return pi

print(round(bellard(1), okr))
#rezult = round(Pi, n)

#print(f"{rezult}")
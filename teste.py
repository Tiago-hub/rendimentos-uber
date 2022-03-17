from re import sub
from decimal import Decimal

needle = "R$"
haystack = "R$ 12"
if needle in haystack:
    print('oi')
"""
Begging
"""

from random import randint

TATICS = [
    'tears stream down your face....', 
    'you offer money and prizes....', 
    'but fear that you might as well be talking to a stuffed parrot....'
]

def beg_for_time():
    print('  ' + TATICS[randint(0,  len(TATICS) - 1)])
    
    return 0 == randint(0,  9)

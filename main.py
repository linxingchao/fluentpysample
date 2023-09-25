from section1.french_deck import FrenchDeck

from collections import namedtuple

import functools
from array import array
import typing
from section8.birds import *

from section9.registration import *
from section9.clockdeco0 import clock

deck = FrenchDeck()

metro_areas = [
    ('Shanghai','CN',35.899,(37.89765677,168.3678289)),
    ('Beijing','CN',28.907,(27.894738,87.9873647)),
    ('Wuhan','CN',47.890,(38.7689374,78.3746589))
]
#print(len(deck))
def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for record in metro_areas:
        match record:
            case [name,_,_,(lat,lon)] if lon <= 0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
                
def memoryview_test():
    octets = array('B',range(6))
    m1 = memoryview(octets)
    l1 = m1.tolist()
    print(l1)
    m2 = m1.cast('B',[2,3])
    l2 = m2.tolist()
    print(l2)
    m3 = m1.cast('B',[3,2])
    l3 = m3.tolist()
    print(l3)
    m2[1,1] = 22
    m3[1,1] = 33
    print(octets)
    
def duck():
    daffy = Duck()
    alert(daffy)
    alert_duck(daffy)
    alert_bird(daffy)
 
@functools.cache
@clock               
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
                
                
                
                
if  __name__ == '__main__':
    print(fibonacci(31))
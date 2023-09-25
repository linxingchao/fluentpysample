from typing import NamedTuple
from dataclasses import dataclass

class Corrdinate:
    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon
        
class Coordinate1(NamedTuple):
    lat:float
    lon:float
    
    def __str__(self):
        ns = 'N' if self.lat>=0 else 'S'
        we = 'E' if self.lon>=0 else 'W'
        return f'{abs(self.lat):.1f} {ns},{abs(self.lon):.1f} {we}'
 
@dataclass(frozen=True)  
class Coordinate2:
    lat:float
    lon:float
    
    def __str__(self):
        ns = 'N' if self.lat>=0 else 'S'
        we = 'E' if self.lon>=0 else 'W'
        return f'{abs(self.lat):.1f} {ns},{abs(self.lon):.1f} {we}'
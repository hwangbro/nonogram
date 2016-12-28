import math

class Point:
    def __init__(self, frac_x: float, frac_y: float):
        self._frac_x = frac_x
        self._frac_y = frac_y
    
    def frac(self) -> (float, float):
        '''Returns the fractional coordinates of the point'''
        
        return (self._frac_x, self._frac_y)

    def pixel(self, size_x: float, size_y: float) -> (float, float):
        '''Returns the pixel coordinates of the point in a given total size'''
        
        return (self._frac_x * size_x, self._frac_y * size_y)


def from_frac(frac_x: float, frac_y: float) -> Point:
    '''Returns a point object with the given fractional coordinates'''
    
    return Point(frac_x, frac_y)

def from_pixel(pixel_x: float, pixel_y: float, size_x: float, size_y: float) -> Point:
    '''Returns a point object with the given pixel coordinates'''
    
    return Point(pixel_x / size_x, pixel_y / size_y)

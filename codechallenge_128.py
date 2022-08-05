'''
Date: 08/05/2022

Task description:
=================
Calculate gear ratio given two or more gears.

Input: radius of gears
Output: gear ratio relative to the first gear

C == 2*Pi*r
Where:
    C	=	circumference
    Pi	=	the constant pi
    r	=	radius of the circle

Psudo Code:
------------
1.  Determine the cercumference of each gear.
2.  Determine the gear ratio.
'''
from decimal import *

class Solution():
    def gearRatio(self, gear_diameters):
        gear_ratio = []
        for i in range(1, len(gear_diameters)):
            gear_ratio.append(Decimal(gear_diameters[i] / gear_diameters[0]))
        return gear_ratio
def main():
    gear_diameters = [1, 2, 3, 4, 5]
    print(Solution().gearRatio(gear_diameters))
main()
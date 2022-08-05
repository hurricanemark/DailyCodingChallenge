'''
Date: 08/05/2022

Task description:
=================
Calculate gear ratio given two or more gears.
A lesson of not to over complicate the problem.

1. Return the ratio relative to the first gear.
2. Return the chanining ratio starting from the first gear.

Input: radius of gears
Output: gear ratio relative to the first gear

C == 2*Pi*r
Where:
    C	=	circumference
    Pi	=	the constant pi
    r	=	radius of the circle

Psudo Code:
------------
1.  Determine the circumference of each gear.
2.  Determine the gear ratio.

Restrospective:
----------------
-  Is it neccessary to calculate the circumference of each gear?
Answer: No.  Since the calculation does not involve non-constant factors, it is not neccessary to calculate the circumference of each gear.
'''
from math import pi
class Solution():
    # calculate the circumference of each gear
    def gearRatio(self, radius: list[float]) -> list[float, dict[float]]:
        gear_ratio = {}
        chaining_ratio = 1

        firstgear_circumference = round(2 * pi * radius[0],2)
        for i in range(1, len(radius)):
            circumference = round(2 * pi * radius[i], 2)
            gear_ratio[i] = circumference / firstgear_circumference 
            chaining_ratio = chaining_ratio / gear_ratio[i]
        return [chaining_ratio, gear_ratio]

    # no need to calculate the circumference of each gear    
    def straightRatio(self, radius: list[float]) -> list[float, dict[float]]:
        straight_ratio = {}
        chaining_ratio = 1
        for i in range(1, len(radius)):
            straight_ratio[i] = radius[i] / radius[0] 
            chaining_ratio = chaining_ratio / straight_ratio[i]
        return [chaining_ratio, straight_ratio]
    
def main():
    ra = [ 2.53, 5.78, 10.44]
    ratios = Solution().gearRatio(ra)
    print("Given three gears with respective radius: {}".format(ra))
    print("Chaining ratio is {}".format(ratios[0]))
    for key in ratios[1]:
        print('\tGear ratio with respect to the first gear is 1 to {}'.format(round(ratios[1][key],2)))

    print("Again, straight ratios:") 
    ratios = Solution().straightRatio(ra)
    print("The chaining ratio is {}".format(ratios[0]))
    for key in ratios[1]:
        print('\tGear ratio with respect to the first gear is 1 to {}'.format(round(ratios[1][key],2)))

if __name__ == "__main__":
    main()        

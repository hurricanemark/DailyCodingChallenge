'''
Decorators return a closure. A closure is what is returned by a decorator.

Basically, a decorator takes in a function, adds some functionality and returns it.


Work-in-progress!!!
'''

class Solution:
   
    def sumOfNumbers(self, nums: list[int]) -> int:
        def listSum(nums):
            if len(nums) == 1:
                return nums[0]
            else:
                return nums[0] + listSum(nums[1:])        
            
        # call the helper function
        return listSum(nums)
    
        
    def productOfNumbers(self, nums: list[int]) -> int:
        def listProduct(nums):
            if len(nums) == 1:
                return nums[0]
            else:
                return nums[0] * listProduct(nums[1:])
        # call the helper function
        return listProduct(nums)

    @staticmethod 
    def fnc(self, nums: list[int]) -> int:
        def listSum(nums):
            if len(nums) == 1:
                return nums[0]
            else:
                return nums[0] + listSum(nums[1:])
        # call the helper function
        return listSum(nums)
    
    @staticmethod
    def fnc2(self, nums: list[int]) -> float:
        x = self.productOfNumbers(nums)
        print(x)
        return x/self.sumOfNumbers(nums)
    
    
def main():
    nums = [1, 2, 3, 4, 5]
    print("Test 1:")
    print("Given array: '{}'".format(nums))
    print("Sum of numbers in the array is {}".format(Solution().sumOfNumbers(nums)))

    nums = [1, 2, 3, 4, 5]
    print("Test 2:")
    print("Given array: '{}'".format(nums))
    print("Product of numbers in the array is {}".format(Solution().productOfNumbers(nums)))

    nums = [1, 2, 3, 4, 5]
    print("Test 3:")
    print("Given array: '{}'".format(nums))
    print("Sum of numbers in the array is {}".format(Solution.fnc(Solution, nums)))

    # nums = [1, 2, 3, 4, 5]
    # print("Test 4:")
    # print("Given array: '{}'".format(nums))
    # print("Product of numbers in the array divided by SumOfNums is {}".format(Solution.fnc2(Solution,nums)))
    
if __name__ == "__main__":
    main()
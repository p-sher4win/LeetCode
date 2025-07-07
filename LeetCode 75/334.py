# Increasing Triplet Subsequence
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        # initialize two variable to infinity
        n1, n2 = float('inf'), float('inf')

        # loop through nums arr
        for n in nums:
            # if n is greater than first and second number return True
            if n > n2:
                return True

            # if n is less than current first, set n to first
            if n <= n1:
                n1=n
            # if n is less than current second, set n to second
            elif n <= n2:
                n2=n
        # if no such number triplet return False
        return False

# Testcases
# nums=[1,2,3,4,5]
# nums = [5,4,3,2,1]
# nums = [2,1,5,0,4,6]
nums = [20,100,10,12,5,13]
s = Solution()
print(s.increasingTriplet(nums))
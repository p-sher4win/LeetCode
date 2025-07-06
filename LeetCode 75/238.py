# Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # initialize the answer list and a variable postfix=1
        ans=[]
        postfix=1

        # loop through the nums arr
        for i in range(0, len(nums)):
            # for index at zero position  
            if i == 0:
                # prefix is 1
                ans.append(1)
            # for index from 1 to n
            else:
                # prefix is the product of prev num in nums arr and the last element in ans arr
                prefix = nums[i-1]*ans[-1]
                ans.append(prefix)

        # loop the nums arr in reverse order
        for i in range(len(nums)-1, -1, -1):
            # for index at last position
            if i == len(nums)-1:
                # postfix is 1
                ans[-1] = ans[i]
            # for index -2 to 0
            else:
                # postfix is product of var postfix into the nums[i+1] arr value 
                postfix*=nums[i+1]
                # new value for the i'th index is product of value at ans[i] into the postfix value
                ans[i] = ans[i] * postfix

        # returns the final ans arr
        return ans

# testcases
nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]
# nums = [0,0]
a = Solution()
print(a.productExceptSelf(nums))
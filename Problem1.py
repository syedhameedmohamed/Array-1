# // Time Complexity : O(n)
# // Space Complexity : O(1)
# // Did this code successfully run on Leetcode : Yes
# // Three line explanation of solution in plain english

# // Your code here along with comments explaining your approach
# Initialize a result array with all values as 1
# Calculate prefix array from left to right (product of all elements to the left of the current element (not including the current element))
# Calculate postfix array from right to left (product of all elements to the right of the current element (not including the current element))
# The resultant array would give the list of elements with every element being the product of all other elements, except itself
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1

        while left < len(nums):
            if left == right:
                right = len(nums)-1
                left+=1
            total = nums[left] + nums[right]
            if total == target:
                return [left,right]
            
            right-=1
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        num_set = set(nums)
        for num in nums:
            seq, curr = 0,num
            while curr in num_set:
                seq +=1
                curr +=1
            count = max(count,seq)
        return count
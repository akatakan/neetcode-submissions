from heapq import heappop, heappush


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_nums = []
        max_heap = []
        for i in range(len(nums)):
            heappush(max_heap,(-nums[i],i))
            if i >= k-1:
                while max_heap[0][1]<=i-k:
                    heappop(max_heap)
                max_nums.append(-max_heap[0][0])
        return max_nums

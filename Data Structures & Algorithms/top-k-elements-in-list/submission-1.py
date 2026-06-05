class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}
        for num in nums:
            if num in frequent:
                frequent[num] +=1
            else:
                frequent[num] = 1
            
        top_list = [(num,freq) for num,freq in frequent.items()]
        top_list.sort(key=lambda x: x[1], reverse=True)

        return [num for num, freq in top_list[:k]]
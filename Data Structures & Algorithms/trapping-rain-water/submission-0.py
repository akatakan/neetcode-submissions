class Solution:
    def trap(self, height: List[int]) -> int:
        L=0
        R=len(height)-1
        max_left=0
        max_right=0
        area=0
        while L <= R:
            if height[L]<height[R]:
                if height[L]>=max_left:
                    max_left=height[L]
                else:
                    area += max_left-height[L]
                L+=1
            else:
                if height[R]>max_right:
                    max_right=height[R]
                else:
                    area += max_right - height[R]
                R-=1
        return area
        


            
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        l=0
        r=len(height)-1

        while l<r:
            w=r-l
            a=min(height[l],height[r])
            area=a*w
            max_area=max(max_area,area)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area
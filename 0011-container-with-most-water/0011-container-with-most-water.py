class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxarea=0
        while l<r:
            h=min(height[l],height[r])
            w=r-l
            maxarea=max(maxarea,h*w)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxarea
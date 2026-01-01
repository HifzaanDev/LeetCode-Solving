class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        area=0
        r=len(height)-1
        while l<r:
            area=max(area,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l=l+1
            elif height[l]>height[r]:
                r=r-1
            elif height[l]==height[r]:
                l=l+1
        return area

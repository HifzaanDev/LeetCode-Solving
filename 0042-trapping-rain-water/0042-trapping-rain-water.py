class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        answer=0
        n=len(height)
        best_l=0
        best_r=0
        l=0
        r=len(height)-1

        while l<r:
            if height[l]<=height[r]:
                
                if height[l]>=best_l:
                    best_l=height[l]
                else:
                    answer=answer+best_l-height[l]
                l=l+1
            if height[l]>height[r]:
                if height[r]>=best_r:
                    best_r = height[r]

                else:
                    answer=answer+best_r-height[r]
                r=r-1
        return answer


                


                
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=0
        max_prof=0
        for i in range(1,len(prices),1):
            if prices[i]-prices[l]>=0 and l<i:
                max_prof=max(max_prof,prices[i]-prices[l])
            elif prices[i]-prices[l]<0 and l<i:
                l=i

        return max_prof

            
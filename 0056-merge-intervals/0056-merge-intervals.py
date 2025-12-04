class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort()
        merged=[]
        merged.append(intervals[0])
        for s,e in intervals[1:]:
            last_s,last_e=merged[-1]
            if s<=last_e:
                merged[-1][1]=max(last_e,e)
            else:
                merged.append([s,e])


        return merged 
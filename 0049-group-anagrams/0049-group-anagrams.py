class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash1={}
        answer=[]
        for ch in strs:
            arr=list(ch)
            sorted_arr=sorted(arr)
            sort_str="".join(sorted_arr)
            if sort_str in hash1:
                hash1[sort_str].append(ch)
            elif sort_str not in hash1:
                hash1[sort_str]=[]
                hash1[sort_str].append(ch)
        for c in hash1:
            answer.append(hash1[c])
        return answer




            



            
            

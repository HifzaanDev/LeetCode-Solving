
from collections import Counter, defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        dict_t = Counter(t)
        required = len(dict_t)
        
        # window counts
        window_counts = defaultdict(int)
        formed = 0
        
        l, r = 0, 0
        ans = (float("inf"), None, None)  # (window length, left, right)
        
        while r < len(s):
            ch = s[r]
            window_counts[ch] += 1
            
            if ch in dict_t and window_counts[ch] == dict_t[ch]:
                formed += 1
            
            # try to contract while window is valid
            while l <= r and formed == required:
                # update answer
                if (r - l + 1) < ans[0]:
                    ans = (r - l + 1, l, r)
                
                # pop from left
                left_char = s[l]
                window_counts[left_char] -= 1
                if left_char in dict_t and window_counts[left_char] < dict_t[left_char]:
                    formed -= 1
                l += 1
            
            r += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]


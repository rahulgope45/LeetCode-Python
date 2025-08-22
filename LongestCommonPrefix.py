class Solution:
    def longestCommonPrefix(self,strs):
        if not strs:
            return ""
        
        prefix =  strs[0]
        for s in strs[1:]:
            while s [:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not strs:
                     return ""
                 
        return prefix
    

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))  # "fl"
print(s.longestCommonPrefix(["dog","racecar","car"]))     # ""
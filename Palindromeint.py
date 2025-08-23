# Palindrome problem for integers

class Solution:
    def palindrome(self, x:int)->bool:
        s = str(x)
        return s == s[::-1]
    
    
s = Solution()
x = 121
y = s.palindrome(x)

print(y)
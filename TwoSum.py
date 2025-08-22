# Two Sum problem
class Solution:
    def twosum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


s = Solution()
print(s.twosum([2,7,11,15], 9))
print(s.twosum([3,2,4], 6))
print(s.twosum([3,3], 6))

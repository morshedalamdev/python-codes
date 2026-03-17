from typing import List

class Solution:
    def largestNum(self, nums: List[int], k: int) -> int:
        max_num = 0
        for x in range(k):
            max_num = max(nums)
            nums.remove(max_num)
            
        return k

sol = Solution()
result1 = sol.largestNum([3,2,1,5,6,4], 2)
result2 = sol.largestNum([3,2,3,1,2,4,5,5,6], 4)
print(result1)
print(result2)
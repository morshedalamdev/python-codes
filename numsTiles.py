from typing import List

class Solution:
    def maxCount(self, nums: List[int]) -> int:
        positive = 0
        negative = 0
        
        for x in nums:
            if x > 0:
                positive += 1
            elif x < 0:
                negative += 1
        return max(positive, negative)

sol = Solution()
input_data = [[-2, -1, -1, 1, 2, 3], [-3,-2,-1,0,0,1,2], [-1, -3, -4], [5,20,66,1314]]
for data in input_data:
    result = sol.maxCount(data)
    print(result)
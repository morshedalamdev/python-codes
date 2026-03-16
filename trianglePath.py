from typing import List

class Solution:
    def trianglePath(self, triangle: List[List[int]]) -> int:
        min_path = 0
        for arr in triangle:
            arr_min = min(arr)
            min_path += arr_min
            
        return min_path

sol = Solution()
result1 = sol.trianglePath([[2],[3,4],[6,5,7],[4,1,8,3]])
result2 = sol.trianglePath([[-10]])
print(result1)
print(result2)
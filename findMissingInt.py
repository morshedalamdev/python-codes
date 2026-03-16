from typing import List

class Solution:
    def findMissingInt(self, arr: List[int], k) -> int:
        last_num = arr[-1]
        missed_int = []
        for num in range(1, last_num):
            if num not in arr:
                missed_int.append(num)
                
        next_num = last_num
        while len(missed_int) < k:
            next_num += 1
            missed_int.append(next_num)
               
        return missed_int[k-1]
        

sol = Solution()
result1 = sol.findMissingInt([2,3,4,7,11], 5)
result2 = sol.findMissingInt([1,2,3,4], 2)
print(result1)
print(result2)
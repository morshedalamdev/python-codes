from typing import List

class Solution:
    def findIsland(self, grid: List[List[str]]) -> int:
        grid_row = len(grid)
        grid_col = len(grid[0])
        count = 0
        
        def dfs(r, c):
            if r < 0 or r >= grid_row or c < 0 or c >= grid_col or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for x in range(grid_row):
            for y in range(grid_col):
                if grid[x][y] == '1':
                    count += 1
                    dfs(x, y)
        
        return count

sol = Solution()
result1 = sol.findIsland([
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
])
result2 = sol.findIsland([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
])
print(result1)
print(result2)
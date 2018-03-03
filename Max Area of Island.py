class Solution:
	def maxAreaOfIsland(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		m = len(grid)
		n = len(grid[0])

		def depthFirstSearch(i,j):
			if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
				grid[i][j] = 0
				return 1 + depthFirstSearch(i-1,j) + depthFirstSearch(i+1,j) + depthFirstSearch(i,j-1) + depthFirstSearch(i,j+1)
			return 0

		area = [ depthFirstSearch(i,j) for i in range(m) for j in range(n) if grid[i][j]]
		if len(area) == 0:
			return 0
		return max(area)

		

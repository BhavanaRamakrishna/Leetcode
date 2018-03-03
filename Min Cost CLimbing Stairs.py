class Solution:
	def minCostClimbingStairs(self, cost):
		"""
		:type cost: List[int]
		:rtype: int
		"""
		#Dp with memoization
		f = [-1 for _ in range(len(cost)+1)]
		def minCost(size):
			if f[size] != -1:
				return f[size]
			if size <= 1:
				f[size] = cost[size]
			else:
				f[size] = cost[size] + min(minCost(size-1), minCost(size-2))
			return f[size]

		return min(minCost(len(cost)-1), minCost(len(cost)-2))


		

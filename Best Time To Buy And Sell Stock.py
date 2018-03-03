class Solution:
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if len(prices) == 1 or len(prices) == 0:
			return 0
		if sorted(prices) == prices:
			return prices[len(prices)-1] - prices[0]
		if sorted(prices, reverse=True) == prices:
			return 0
		#kadane's algorithm
		nums = [prices[i]-prices[i-1] for i in range(len(prices)-1,0,-1)]
		print(nums)
		if len(nums) == 1:
			return nums[0]
		current_max = nums[0]
		global_max = nums[0]
		cs = 0
		gs = 0
		ge = 0
		ce = 0
		for i in range(1,len(nums)):
			if current_max + nums[i] < nums[i]:
				current_max = nums[i]
				cs = i
				ce = i
			else:
				current_max += nums[i]
				ce = i
			if current_max > global_max:
				global_max = current_max
				gs = cs
				ge = ce
		return global_max

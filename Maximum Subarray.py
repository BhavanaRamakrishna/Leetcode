class Solution:
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		#kadane's algorithm
		assert len(nums) != 0
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

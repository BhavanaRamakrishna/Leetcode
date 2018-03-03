class Solution:
	def findLengthOfLCIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		#using kadane's algorithm intuition
		if len(nums) <= 1:
			return len(nums)
		current_count = 1
		global_count = 1
		for i in range(1,len(nums)):
			if nums[i] > nums[i-1]:
				current_count += 1
			else:
				current_count = 1
			if current_count > global_count:
				global_count = current_count;
		return global_count

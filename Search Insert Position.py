class Solution:
	def searchInsert(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		if target in nums:
			return nums.index(target)
		else:
			for i,value in  enumerate(nums):
				if value >target:
					return i
			return len(nums)

class Solution:
	def removeElement(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		"""
		count = 0
		for i, value in enumerate(nums):
			print(nums)
			if value == val:
				nums[i] = -1
		while -1 in nums:
			nums.remove(-1)
			print(nums)
		return len(nums)


				

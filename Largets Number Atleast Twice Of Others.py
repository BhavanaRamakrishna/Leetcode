class Solution:
	def dominantIndex(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 0 or len(nums) == 1:
			return 0
		s = list.copy(nums)
		s.sort()
		if s[len(s)-1] >= 2*s[len(s)-2]:
			return nums.index(s[len(s)-1])
		return -1
	

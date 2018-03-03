class Solution:
	def missingNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums.sort()
		n = len(nums)
		j = 0
		for i in range(n-1,-1,-1):
			if nums[i] != n-j :
				return n-j
			j +=1
		return 0
		

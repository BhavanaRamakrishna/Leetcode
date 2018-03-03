class Solution:
	def twoSum(self, numbers, target):
		"""
		:type numbers: List[int]
		:type target: int
		:rtype: List[int]
		"""
		i = 0
		j = len(numbers)-1
		while True:
			psum = numbers[i] + numbers[j]
			if psum == target:
				return [i+1, j+1]
			elif psum > target:
				j -= 1
			else:
				i += 1
		return i,j
				

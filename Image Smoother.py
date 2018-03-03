class Solution:
	def imageSmoother(self, M):
		"""
		:type M: List[List[int]]
		:rtype: List[List[int]]
		"""
		solution = [[0] * len(M[0]) for _ in M]
		for r in range(0,len(M)):
			for c in range(0,len(M[0])):
				#get count
				one_count = 0
				all_count = 0
				for i in (r-1,r,r+1):
					for j in (c-1,c,c+1):
						if 0<=i<len(M) and 0<=j<len(M[0]):
							all_count += 1
							if M[i][j] != 0:
								one_count += M[i][j]
				solution[r][c] = math.floor(one_count/all_count)
		return solution

hashmap = {}
		for x in nums:
			if x in hashmap:
				hashmap[x] += 1
			else:
				hashmap[x] = 1
			if hashmap[x] > math.floor(len(nums)/2):
					return x

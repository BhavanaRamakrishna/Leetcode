str1 = ''.join(str(x) for x in bits)
		newList = [int(i) for i in re.findall(r'[0]|[1][0-1]', str1)]
		if newList[len(newList)-1] == 0:
			return True
		return False

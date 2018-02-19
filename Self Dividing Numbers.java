class Solution {
	public List<Integer> selfDividingNumbers(int left, int right) {
		ArrayList<Integer> list = new ArrayList<Integer>();
		for(int i=left; i<=right; i++){
			int n = i;
			int flag = 0;
			while(n>0){
				int r = n%10;
				if(r==0){
					flag =1;
					n=n/10;
					break;
				}

				if(i%r!=0){
						flag=1;
					break;
				}
				n = n/10;
			}
			if(flag==0)
				list.add(i);
		}
		return list;
	}
}

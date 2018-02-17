class Solution {
	public boolean detectCapitalUse(String word) {
		int i=0, cap=0, allcap=0, low=0;
		char[] array = word.toCharArray();
		if(array.length==1)
			return true;
		if(Character.isUpperCase(array[i])){
			if(Character.isUpperCase(array[i+1]))
				allcap = 1;
			else
				cap = 1;
		}
		else{
			low = 1;
			if(Character.isUpperCase(array[i+1]))
				low = 0;
		}
		for(i=2; i<array.length;i++){
			if(Character.isUpperCase(array[i])){
				cap =0;
				low =0;
			}
			else{
				allcap=0;
			}
		}
		return(cap==1 || allcap==1 || low==1 );
	}
}

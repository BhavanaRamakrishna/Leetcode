class Solution {
	public String reverseWords(String s) {
		StringBuilder sb;
		StringBuilder output = new StringBuilder();
		String[] words = s.split("\\s+");
		for(String word:words){
			sb = new StringBuilder(word);
			sb.reverse();
			output.append(sb);
			output.append(" ");
		}
		return String.valueOf(output).trim();
	}
}

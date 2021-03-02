import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		sc.nextLine();
		
		for(int tc = 1; tc <= T; tc++) {
			String word = sc.nextLine();
			String[] array_word = word.split("");
			ArrayList<String> words = new ArrayList<String>();
			ArrayList<String> stack = new ArrayList<String>();
			
			for(String s:array_word) {
				words.add(s);
			}
			for(String w:words) {
				if(!stack.contains(w)) {
					stack.add(w);
				}
			}
			System.out.format("#%d %d\n", tc, stack.size());
			//			System.out.println(array_word[2]);
		}

	}

}

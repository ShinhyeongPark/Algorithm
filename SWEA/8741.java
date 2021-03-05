import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt(); //Test Case
		sc.nextLine();
		
		for(int tc = 1; tc <= T; tc++) {
			String[] strarr;
			String answer = "";
			
			String str = sc.nextLine();
			strarr = str.split(" ");
			for (int i = 0; i < 3; i ++) {
				String s = strarr[i].substring(0,1);
				s = s.toUpperCase();
				answer += s;
			}	
			System.out.format("#%d %s\n", tc, answer);
		}
	}
}

import java.util.Scanner;

class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); //Case 수 입력 
		for(int tc=1; tc<=T; tc++) {
			int L = sc.nextInt(); //String Length
			String str1 = sc.next();
			String str2 = sc.next();
			
			int C = 0;
			for(int i = 0; i < L; i++) {
				if(str1.charAt(i) == str2.charAt(i)) {
					C += 1;
				}
			}
			System.out.format("#%d %s\n", tc, C);
		}
	}
}

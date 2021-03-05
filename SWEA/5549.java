import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Solution {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); //Test Case
		sc.nextLine();
		for(int tc = 1; tc <= T; tc++) {
			String N = sc.nextLine(); //Int to String
			int n = Integer.parseInt(N.substring(N.length()-1)); //String Last Char
			
			if (n % 2 == 0) {
				System.out.format("#%d Even\n", tc);
			}
			else {
				System.out.format("#%d Odd\n", tc);
			}
		}
	}
}

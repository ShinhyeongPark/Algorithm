import java.util.Scanner;

class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); //Test Case
		for(int tc = 1; tc <= T; tc++) {
			String str = sc.next();
			Boolean flag1 = true;
			Boolean flag2 = true;
			
			int x = Integer.valueOf(str.substring(0,2));
			int y = Integer.valueOf(str.substring(2,4));
			
			if(x > 12 || x < 1) {
				flag1 = false;
			}
			
			if(y > 12 || y < 1) {
				flag2 = false;
			}
			
			if(flag1 == true && flag2 == true) {
				System.out.format("#%d AMBIGUOUS\n", tc);
			}
			else if(flag1 == true && flag2 == false) {
				System.out.format("#%d MMYY\n", tc);
			}
			else if(flag1 == false && flag2 == true) {
				System.out.format("#%d YYMM\n", tc);
			}
			else {
				System.out.format("#%d NA\n", tc);
			}
		}
	}
}

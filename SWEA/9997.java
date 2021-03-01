import java.util.Scanner;

class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc = 1; tc <= T; tc++) {
			int Time = sc.nextInt();
			int Hour = Time / 30;
			int Min = (Time - (Hour * 30)) * 2;
			
			System.out.format("#%d %s %s\n", tc, Hour, Min);
		}
	}

}

import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;

class Solution {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); //Test Case
		sc.nextLine();

		for(int tc = 1; tc <= T; tc++) {
			String str = sc.nextLine(); //양옆에 좌석 수 입력 2 3 2
			String[] array = str.split(" "); //2,3,2
			
			ArrayList<Integer> num = new ArrayList<Integer>();
			
			for(String s:array) {
				num.add(Integer.parseInt(s));
			} //0:L, 1: U, 2: X
			
			if(num.get(2) < num.get(0)) {
				System.out.format("#%d %d\n", tc, num.get(0) - num.get(2));
			}
			else if(num.get(2) > num.get(1)) {
				System.out.format("#%d %d\n", tc, -1);
			}
			else {
				System.out.format("#%d %d\n", tc, 0);
			}
		}
	}
}

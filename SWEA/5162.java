import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;
import java.util.Collections;

class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt(); //Test Case
		
		for(int tc = 1; tc <= T; tc++) {
			int A = sc.nextInt(); //3
			int B = sc.nextInt(); //5
			int C = sc.nextInt();
			
			int Min = 0;
			if (A < B) {
				Min = A;
			}
			else {
				Min = B;
			}
			System.out.format("#%d %d \n", tc, C/Min);
			
		}
	}
}

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
			int N = sc.nextInt(); //2
			
			double Sum = 0;
			for (int i = 0; i < N; i++) {
				float p = sc.nextFloat();
				int money = sc.nextInt();
				
				Sum += p * (double)money;
			}
			
			System.out.format("#%d %.6f \n", tc, Sum);
			
		}
	}
}

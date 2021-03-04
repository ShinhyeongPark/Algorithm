import java.util.ArrayList;
import java.util.Scanner;

class Solution {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); //Test Case
		
		for(int tc = 1; tc <= T; tc++) {
			int[] scores = new int[5];
			
			for (int i = 0; i < 5; i++) {
				scores[i] = sc.nextInt();
			}
      
			int sum = 0;
			for (int j = 0; j < 5; j++) {
				if (scores[j] < 40) {
					sum += 40;
				}
				else {
					sum += scores[j];
				}
			}
      
			System.out.format("#%d %d\n", tc, sum/5);
		}	
	}
}

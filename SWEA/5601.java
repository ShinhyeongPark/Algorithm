import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;

class Solution {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); //Test Case
		
		for(int tc = 1; tc <= T; tc++) {
			int N = sc.nextInt();
			
			System.out.print("#" + tc);
			for (int i = 0; i < N; i++) {
				System.out.print(" 1/"+N);
			}
      System.out.println();
		}
			
	}
}

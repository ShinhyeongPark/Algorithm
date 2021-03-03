import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;

class Solution {
	public static int powfunc(int x, int y) {
		return x * y;
	}
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int T = 10;
		
		for(int tc = 1; tc <= T; tc++) {
			int n = sc.nextInt();
			int[] x = new int[2];
			
			for(int i = 0; i < 2; i++) {
				x[i] = sc.nextInt();
			}
			
			int mul = x[0];
			for(int j = 0; j < x[1] - 1; j++) {
				x[0] = powfunc(x[0],mul);
			}
			System.out.format("#%d %d \n", n, x[0]);
		}
	}
}

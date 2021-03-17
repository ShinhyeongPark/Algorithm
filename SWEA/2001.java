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
			int N = sc.nextInt(); //array size
			int M = sc.nextInt(); //catch size
			
			int[][] array = new int[N][N]; //4X4
			
			for (int i = 0; i<N; i++) {
				for (int j = 0; j < N; j++) {
					array[i][j] = sc.nextInt();
				}
			}
			
			int Max = 0;
			int Sum = 0;
			for (int i = 0; i <= N-M; i++) {
				for (int j = 0; j <= N-M; j++) {
					//Start Point 좌표
					Sum = 0;
					for (int k = 0; k < M; k++) {
						for (int w = 0; w < M; w++) {
							Sum += array[i+k][j+w];	
						}
					}
					if (Sum >= Max) {
						Max = Sum;
					}
				}
			}
			System.out.format("#%d %d\n", tc,Max);
			
		}
	}
}

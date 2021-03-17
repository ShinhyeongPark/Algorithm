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
			int N = sc.nextInt(); //4 Line
			
			int[][] array = new int[N][N]; //4X4
			
			array[0][0] = 1;
			
			for (int i = 1; i < N; i++) {
				for (int j = 0; j < i+1; j++) {
					if (j == 0) {
						array[i][j] = 1;
					}
					else if (j == i){
						array[i][j] = 1;
					}
					else {
						array[i][j] = array[i-1][j-1] + array[i-1][j];
					}
					
				}
			}
			System.out.format("#%d \n", tc);
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < i+1; j++) {
					if (j == i) {
						System.out.format("%d\n", array[i][j]);
					}
					else {
						System.out.format("%d ", array[i][j]);
					}
				}
			}
		}
	}
}

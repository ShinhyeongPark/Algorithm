
import java.util.ArrayList;
import java.util.Scanner;


class Solution {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); //Test Case
		
		for(int tc = 1; tc <= T; tc++) {
			int N = sc.nextInt(); //Person
			int M = sc.nextInt(); //Problem
			int[][] array = new int[N][M];
			int[] solnum = new int[N];
			
			for (int i = 0; i < N; i ++) {
				for (int j = 0; j < M; j ++) {
					array[i][j] = sc.nextInt();
				}
			}
			
			for (int k = 0; k < N; k ++) { //한 사람당 맞은 갯수 저장 
				int count = 0;
				
				for (int x = 0; x < M; x ++) {
					if (array[k][x] == 1) {
						count += 1;
					}
					solnum[k] = count;
				}
			}
			
			int first_num = 0;
			for (int i = 0; i < N; i ++) { //가장 많이 맞은 갯수 찾기 
				if (first_num < solnum[i]) {
					first_num = solnum[i];
				}
			}
			int first_person = 0;
			for (int j = 0; j < N; j ++) {
				if (solnum[j] == first_num) {
					first_person += 1;
				}
			}
			System.out.format("#%d %d %d\n", tc, first_person, first_num);
			
			
			
		}	
	}
}

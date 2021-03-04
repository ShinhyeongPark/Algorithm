package com.example;
import java.util.ArrayList;
import java.util.Scanner;


public class Solution {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); //Test Case
		
		for(int tc = 1; tc <= T; tc++) { 
			int N = sc.nextInt(); //농장 크기 
			sc.nextLine();
			
			String number; //문자열로 값을 입력 
			int[][] array = new int[N][N]; //농장을 배열로 표현 
			for (int i = 0; i < N; i++) {
				number = sc.nextLine();
				String[] num = number.split("");
				
				for (int j = 0; j < N; j++) {
					array[i][j] = Integer.parseInt(num[j]);
				}
			}
			
			int sum = 0;
			int mid = N/2;
			
			
			for (int i = 0; i < mid; i++) {
				for (int j = mid - i; j <= mid + i; j++) {
					sum += array[i][j];
				}
			}
			for (int i = mid; i >= 0; i--) {
				for (int j = mid - i; j <= mid + i; j++) {
					sum += array[N-i-1][j];
				}
			}
			
			System.out.format("#%d %d\n", tc, sum);
			
		}	
	}
}

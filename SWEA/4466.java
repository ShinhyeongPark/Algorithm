package com.example;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); //Test Case
		
		for(int tc = 1; tc <= T; tc++) {
			int N = sc.nextInt(); //Class Num
			int K = sc.nextInt(); //Select Num
			
			List<Integer> stack = new ArrayList<Integer>(); //Each Class Score
			
			for (int i = 0; i < N ; i++) {
				int K_num = sc.nextInt();
				stack.add(K_num);
			}
			
			int sum = 0; //Max Sum Score
			for (int j = 0; j < K; j++) { //Select Num
				int Max = 0;
				for (int i = 0; i < N - j; i++) { //Find Max Score
					if (stack.get(i) > Max) {
						Max = stack.get(i);
					}
				}
				sum += Max;
				stack.remove((Integer)Max);
			}
			System.out.format("#%d %d\n", tc, sum);
		}
	}
}

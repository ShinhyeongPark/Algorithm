package com.example;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class Solution {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); //Test Case
		
		for(int tc = 1; tc <= T; tc++) { 
			int[] arr = new int[3];
			
			for (int i = 0; i < 3; i++) {
				arr[i] = sc.nextInt();
			}
			
			List<Integer> x = new ArrayList<Integer>();
			List<Integer> stack = new ArrayList<Integer>();
			for (int i = 0; i <3; i++) {
				x.add(arr[i]);
			}
			
			for (int i = 0; i < 3; i++) {
				if (stack.contains(x.get(i))) {
					stack.remove(x.get(i));
				}
				else {
					stack.add(x.get(i));
				}
			}
			System.out.format("#%d %d\n", tc, stack.get(0));
			
		}	
	}
}

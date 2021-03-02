package com.example;
import java.util.ArrayList;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); //Test Case
		for(int tc = 1; tc <= T; tc++) {
			ArrayList<Character> stack = new ArrayList<Character>();
			String str = sc.next();
			
			for(int i = 0; i < str.length(); i++) {
				if (stack.contains(str.charAt(i))) { //스택에 있을 경우
//					System.out.println("T");
					stack.remove(stack.indexOf(str.charAt(i)));
				}
				else {
//					System.out.println("F");
					stack.add(str.charAt(i));
				}
			}
//			System.out.println(stack);
			System.out.format("#%d %d\n", tc, stack.size());
		}
	}
}

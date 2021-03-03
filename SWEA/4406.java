package com.example;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;

public class Solution {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); //Test Case
		sc.nextLine();
		
		for(int tc = 1; tc <= T; tc++) {
			String str = sc.nextLine();
			String answer = "";
			
			for(int i = 0; i < str.length(); i++) {
				if(str.charAt(i) != 'a' && str.charAt(i) != 'e' && str.charAt(i) != 'i' && str.charAt(i) != 'o' && str.charAt(i) != 'u') {
					answer += str.charAt(i);
				}
			}

			System.out.format("#%d %s\n", tc, answer);
		}
	}
}

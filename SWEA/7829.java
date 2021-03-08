package com.example;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;
import java.util.Collections;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt(); //Test Case
		
		for(int tc = 1; tc <= T; tc++) {
			int N = sc.nextInt();
			List<Integer> pwd = new ArrayList<Integer>();
			
			for (int i = 0; i < N; i++) {
				int p = sc.nextInt();
				pwd.add(p);
			}
			Collections.sort(pwd); //리스트 오름차순 정
			//결국 우릭라 구하고자하는 값은 약수만을 확인하여 비밀번호를 구하는 것 
			//약수를 정렬했을 때, 첫번째값과 마지막 값을 곱하면 비밀번호가 된다 
			System.out.format("#%d %d \n", tc, pwd.get(0)*pwd.get(pwd.size()-1));
			
		}
	}
}

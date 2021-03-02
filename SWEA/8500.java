package com.example;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); //Test Case
		for(int tc = 1; tc <= T; tc++) {
			int N = sc.nextInt(); //사람 수
			sc.nextLine();

			String str = sc.nextLine(); //양옆에 좌석 수 입력 2 3 2
			String[] array = str.split(" "); //2,3,2
			
			ArrayList<Integer> num = new ArrayList<Integer>();
			
			for(String s:array) {
				num.add(Integer.parseInt(s));
			}
			Collections.sort(num);
			
			int count = 0;
			int temp = 0;
			for(Integer n:num) {
				if(count == 0) {
					count += 2 * n + 1;
					temp = n; //이전 값 저장 
				}
				else {
					if(temp != n) { //이전 값과 다를 경우 
						count += (n - temp) + 1 + n;
						temp = n;
					}
					else { //이전값과 같을 경
						count += 1 + n ;
						temp = n;
					}
				}
			}
			System.out.format("#%d %d\n", tc, count);
		}
	}
}

//알고리즘 
//1. 가능한 극장 좌석의 최소 갯수를 구하는 것이기 때문에 오름차순 정렬 
//2.정렬된 리스트에서 이전값과 같을 경우와 다를 경우로 나눠진다.
//3. 다를 경우에는 이전값과의 차이(n-temp), 자기좌석(1), 자기의 번호만큼(n) 더한다.
//4. 같을 경우, 내 옆에 이미 자기 번호만큼 비어있으므로 자기좌석과 자기의 번호만큼만 더한다.

import java.util.ArrayList;
import java.util.Scanner;

class Solution {
  //문자열 각 자리수를 Int로 변환 후 더한 값을 리턴하는 함수
	public static int summutation(String str) {
		int answer = 0;
		for(int i = 0; i < str.length(); i++) {
			answer += Character.getNumericValue(str.charAt(i));
		}
		return answer;	
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); //Test Case
		sc.nextLine(); //숫자를 입력받고 문자열을 입력받으려면 반드시 공백을 한번 제거
		for(int tc = 1; tc <= T; tc++) {
			String str = sc.nextLine();
			String[] array = str.split(" "); //공백으로 분리
			
//			System.out.println(array[1]);
			int max = summutation(array[0]);
			int min = summutation(array[0]);
			
			for(int i = 1; i < array.length; i++) {
				int res = summutation(array[i]);
				if(res > max) {
					max = res;
				}
				if(res <min) {
					min = res;
				}
			}
//			System.out.println(stack);
			System.out.format("#%d %d %d\n", tc, max, min);
		}
	}
}

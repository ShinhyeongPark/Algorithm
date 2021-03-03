import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;

class Solution {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); //Test Case
		

		for(int tc = 1; tc <= T; tc++) {
			int N = sc.nextInt();
			sc.nextLine();
			
			String str = sc.nextLine(); //블록 높이 
			String[] array = str.split(" "); //띄어쓰기 분리 
			
			ArrayList<Integer> num = new ArrayList<Integer>(); //String을 정수로 변환 
			ArrayList<Integer> difficulty_up = new ArrayList<Integer>(); //높이가 증가하는 난이도 리스트
			ArrayList<Integer> difficulty_down = new ArrayList<Integer>(); //높이가 낮아지는 난이도 리스트
			
      //정수로 변환한 값을 저장
			for(String s:array) {
				num.add(Integer.parseInt(s));
			}
      
      //높이가 증가할 경우 up리스트에, 낮아질 경우에는 down리스트에 난이도 차이를 저장
			for(int i =0; i < N-1; i++) {
				if(num.get(i+1)-num.get(i) > 0) {
					difficulty_up.add(num.get(i+1)-num.get(i));
				}
				else {
					difficulty_down.add(num.get(i+1)-num.get(i));
				}
			}
      
			int dmax = 0;
			int dmin = 0;
      
      
      
			if(difficulty_up.size(오 == 0) {
				dmax = 0;
			}
			else {
				dmax = Collections.max(difficulty_up);
			}
			
			if(difficulty_down.size() == 0) {
				dmin = 0;
			}
			else {
				dmin = Math.abs(Collections.min(difficulty_down));
			}
			System.out.format("#%d %d %d\n", tc, dmax, dmin);
		}
	}
}

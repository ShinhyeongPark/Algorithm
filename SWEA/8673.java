import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;

class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); //Test Case
		
		for(int tc = 1; tc <= T; tc++) {
			int K = sc.nextInt(); //사람 수
			sc.nextLine();

			String str = sc.nextLine(); //양옆에 좌석 수 입력 2 3 2
			String[] array = str.split(" "); //2,3,2
			
			ArrayList<Integer> num = new ArrayList<Integer>();
			ArrayList<Integer> winner = new ArrayList<Integer>();
			
			for(String s:array) {
				num.add(Integer.parseInt(s));
			} //7,1,4,3
			
			int sum = 0;
			
			while(winner.size() != 1) {
				winner = new ArrayList<Integer>();
				for(int i =0; i<num.size(); i+= 2) {
//					System.out.println(i);
					sum += Math.abs(num.get(i)-num.get(i+1));
					if(num.get(i) >= num.get(i+1)) {
						winner.add(num.get(i));
					}
					else {
						winner.add(num.get(i+1));
					}
				}
				num.clear();
				num.addAll(winner);
			}
			System.out.format("#%d %d\n", tc, sum);
		}
	}
}

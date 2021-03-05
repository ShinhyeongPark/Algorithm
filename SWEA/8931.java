import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt(); //Test Case
		
		for(int tc = 1; tc <= T; tc++) {
			int N = sc.nextInt();
			List<Integer> stack = new ArrayList<Integer>();
			
			int sum = 0;
			for (int i = 0; i < N; i++) {
				int n = sc.nextInt();
				
				if (n != 0) {
					stack.add(n);
				}
				else {
					stack.remove(stack.size()-1);
				}
			}
			
			for (int j = 0; j < stack.size(); j++) {
				sum += stack.get(j);
			}
			
			System.out.format("#%d %d \n", tc, sum);
			
		}
	}
}

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Solution {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); //Test Case
		
		for(int tc = 1; tc <= T; tc++) {
			int N = sc.nextInt(); //Student
			int K = sc.nextInt(); //OK_Student
			
			List<Integer> stack = new ArrayList<Integer>();
			for (int i = 0; i < N ; i++) {
				stack.add(i+1);
			}
//			System.out.println(stack);
			for (int j = 0; j < K; j++) {
				int K_num = sc.nextInt();
				stack.remove((Integer)K_num);
			}
			System.out.print("#"+tc);
			for (int x = 0; x < stack.size(); x++) {
				System.out.print(" " + stack.get(x));
			}
			System.out.println();
		}	
	}
}

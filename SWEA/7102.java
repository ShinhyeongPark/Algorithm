import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;
import java.util.Collections;

class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt(); //Test Case
		
		for(int tc = 1; tc <= T; tc++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			
			List<Integer> Narr = new ArrayList<Integer>();
			List<Integer> Marr = new ArrayList<Integer>();
			List<Integer> Sumarr = new ArrayList<Integer>();
			List<Integer> High = new ArrayList<Integer>();
			List<Integer> Value = new ArrayList<Integer>();
			List<Integer> Answer = new ArrayList<Integer>();

			int sum = 0;
			for (int i = 1; i <= N; i++) {
				Narr.add(i);
			}
			
			for (int j = 1; j <= M; j++) {
				Marr.add(j);
			}
			
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					Sumarr.add(Narr.get(i) + Marr.get(j));
				}
			}
			Collections.sort(Sumarr);
			
			while (!Sumarr.isEmpty()) {
				int x = Sumarr.get(0); //리스트 시작원소 저장
				int count = 0;
				while (Sumarr.contains(x)) {
					Sumarr.remove((Integer)x);
					count += 1;
				}
				Value.add(x);
				High.add(count);
			}

			
			int HighMax = 0;
			for (int i = 0; i < High.size(); i++) {
				if (HighMax < High.get(i)) {
					HighMax = High.get(i);
				}
			}

			for (int j = 0; j < High.size(); j++) {
				if (HighMax == High.get(j)) {
//					System.out.println(Value.get(j));

					Answer.add(Value.get(j));
				}
			}

			System.out.print("#" + tc);
			for (int i = 0; i < Answer.size(); i++) {
				System.out.print(" " + Answer.get(i));
			}
            System.out.println();
//			System.out.format("#%d %d \n", tc, sum);
			
		}
	}
}

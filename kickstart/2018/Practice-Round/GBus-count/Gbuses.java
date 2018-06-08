import java.util.Arrays;
import java.util.Scanner;

public class Gbuses {
	static Scanner in = new Scanner(System.in);
	
	static void solution(){
		int T = in.nextInt();
		for(int caseNum = 1; caseNum <= T; caseNum++){
			int[] city = new int[5001];
			Arrays.fill(city, 0);
			int N = in.nextInt();
			for(int i = 0; i < N; i++){
				int ai = in.nextInt();
				int bi = in.nextInt();
				
				for(int j = ai; j <= bi; j++){
					city[j]++;
				}
			}
			
			System.out.printf("Case #%d:", caseNum);
			
			int P = in.nextInt();
			for(int i = 1; i <= P; i++){
				int bus = in.nextInt();
				System.out.printf(" %d", city[bus]);
			}
			
			System.out.println();
		}
		
	}
	public static void main(String[] args) {
		solution();
	}
}

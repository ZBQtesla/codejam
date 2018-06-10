/**
 * leetcode problem 650
 * @author Baiqiang
 */
import java.util.*;

public class KeysKeyboard{
	static Scanner in = new Scanner(System.in);
	static void solution(){
		int n = in.nextInt();
		int had = 1;
		int left = n - 1;
		int num = 0;
		int copy = 1;
		while(left > 0){
			if(left % had == 0){
				num += 2;
				left -= had;
				copy =  had;
				had = had << 1;
			}
			else{
				left -= copy;
				had += copy;
				num++;
			}
		}
		System.out.println(num);
	}
	public static void main(String[] args) {
		solution();
	}
}

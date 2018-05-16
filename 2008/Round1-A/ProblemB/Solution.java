import java.util.Arrays;
import java.util.Scanner;

/**
 * 
 */

/**
 * @author baiqiang
 *
 */
public class Solution {
    static Scanner in = new Scanner(System.in);

    static void solution() {
        int C = in.nextInt();

        for (int caseId = 1; caseId <= C; caseId++) {
            int N = in.nextInt();
            int M = in.nextInt();

            int[][] likedType = new int[M][N];
            boolean[][] like = new boolean[M][N];
            boolean[] deletedCus = new boolean[M];
            int deletedNum = 0;

            int[] likedNum = new int[M];
            int[] result = new int[N];
            Arrays.fill(result, 0);
            for (int cnt = 0; cnt < M; cnt++) {
                Arrays.fill(like[cnt], false);
            }
            Arrays.fill(deletedCus, false);

            for (int i = 0; i < M; i++) {
                int T = in.nextInt();
                likedNum[i] = T;
                for (int t = 0; t < T; t++) {
                    int flavor = in.nextInt();
                    int type = in.nextInt();
                    likedType[i][flavor - 1] = type;
                    like[i][flavor - 1] = true;
                }
            }

            // result
            System.out.printf("Case #%d:", caseId);
            boolean im = false;
            aCase: 
            while (deletedNum != M) {
                int only = 0;
                for (int cus = 0; cus < M; cus++) {
                    if (likedNum[cus] == 1 && !deletedCus[cus]) {
                        for (int flavor = 0; flavor < N; flavor++) {
                            if (like[cus][flavor] && likedType[cus][flavor] == 1) {
                                only++;
                                result[flavor] = 1;
                                for (int cusP = 0; cusP < M; cusP++) {
                                    if (like[cusP][flavor] && !deletedCus[cusP]) {
                                        if (likedNum[cusP] == 1 && likedType[cusP][flavor] == 0) {
                                            System.out.print(" IMPOSSIBLE");
                                            im = true;
                                            break aCase;
                                        } else if (likedType[cusP][flavor] == 1) {
                                            deletedCus[cusP] = true;
                                            deletedNum++;
                                        } else if(likedType[cusP][flavor] == 0){
                                            like[cusP][flavor] = false;
                                            likedNum[cusP]--;
                                        }
                                    }
                                }
                                break;
                            }
                        }
                    }
                }
                if(only ==  0)
                    break;
            }

            if (!im) {
                for (int r : result) {
                    System.out.printf(" %d", r);
                }
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        solution();
    }
}

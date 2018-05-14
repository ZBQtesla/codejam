import java.util.Arrays;
import java.util.Scanner;

/**
 * 
 */

/**
 * @author baiqiang
 *
 */
public class A {
    static Scanner in = new Scanner(System.in);

    static int T;

    static void solution() {
        T = in.nextInt();

        for (int i = 0; i < T; i++) {
            int n = in.nextInt();
            Long[] X = new Long[n];
            Long[] Y = new Long[n];

            for (int j = 0; j < n; j++) {
                X[j] = in.nextLong();
            }
            for (int j = 0; j < n; j++) {
                Y[j] = in.nextLong();
            }

            Arrays.sort(X, (a, b) -> {
                return (int) (b - a);
            });

            Arrays.sort(Y, (a, b) -> {
                return (int) (a - b);
            });

            long sum = 0;
            for (int j = 0; j < n; j++) {
                sum += X[j] * Y[j];
            }

            System.out.printf("Case #%d: %d %n", i + 1, sum);

        }

    }

    public static void main(String[] args) {
        solution();
    }
}

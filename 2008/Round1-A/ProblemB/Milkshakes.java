import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

/**
 * 
 */

/**
 * @author baiqiang
 *
 */
public class Milkshakes {
    static final Scanner in = new Scanner(System.in);
    static int C;

    static void solution() {
        C = in.nextInt();

        for (int i = 0; i < C; i++) {
            int N = in.nextInt();
            int M = in.nextInt();

            List<customer> allcstmer = new ArrayList<>();

            int[] milk = new int[N + 1];
            Arrays.fill(milk, -1);

            for (int j = 0; j < M; j++) {
                int T = in.nextInt();
                customer ctmer = new customer(T, N);
                for (int k = 0; k < T; k++) {
                    int t1 = in.nextInt();
                    int t2 = in.nextInt();
                    ctmer.type[t1] = t2;
                    allcstmer.add(ctmer);
                }
            }

            allcstmer.sort((a, b) -> {
                return a.T - b.T;
            });
            boolean im = false;
            for (customer c : allcstmer) {
                boolean breakflag = false;
                int first = 0;
                int malted = 0;
                for (int ii = 1; ii <= N; ii++) {
                    if (c.type[ii] == -1) {
                        continue;
                    } else if (c.type[ii] == milk[ii]) {
                        breakflag = true;
                        break;
                    } else if (milk[ii] == -1 && (first == 0 || malted == 1)) {
                        first = ii;
                    }
                }

                if (!breakflag && first != 0) {
                    if (milk[first] != -1) {
                        im = true;
                        break;
                    }
                    milk[first] = c.type[first];
                }
            }

            if (im) {
                System.out.println("Case #" + (i + 1) + ": IMPOSSIBLE");
            }
            
            for(int j = 0; j <= N; j++) {
                if(milk[j] == -1) {
                    milk[j] = 0;
                }
            }
            
            System.out.printf("Case #%d: %d", i + 1, milk[1]);
            for (int ii = 2; ii <= N; ii++) {
                System.out.printf(" %d", milk[ii]);
            }
            System.out.println();
        }

    }

    public static void main(String[] args) {
        solution();
    }
}

class customer {
    int T;
    int[] type;

    /**
     * 
     */
    public customer(int T, int N) {
        this.T = T;
        type = new int[N + 1];
        Arrays.fill(type, -1);
    }
}
import java.util.Scanner;

/**
 * @author baiqiang
 *
 */
public class Stall {
    static Scanner in = new Scanner(System.in);

    /*
     * Rounded up.
     */
    static long ceil(long n) {
        if (n < 0)
            return 0;
        return (n >> 1) + (n & 0x1);
    }

    /*
     * Rounded down.
     */
    static long floor(long n) {
        if (n < 0)
            return 0;
        return n >> 1;
    }

    /*
     * The numbers of floor.
     */
    static long numOfFloor(long n) {
        long num = 0;
        while (n != 1) {
            n = n >> 1;
            num++;
        }
        return num;
    }

    static void solution() {
        int T = 0;
        T = in.nextInt();
        for (int i = 1; i <= T; i++) {
            long N = in.nextLong();
            long K = in.nextLong();
            
            // floor should be long
            long floor = numOfFloor(K);
            
            // Wow! Wow! Wow! Evil java! 
            long tmp = 1;
            long indexOfFloor = (K + 1 - (tmp << floor));

            long min = 0;
            long max = 0;


            Segment currMin = new Segment(0, 0);
            Segment currMax = new Segment(N, 1);

            Segment nextMin = new Segment(0, 0);
            Segment nextMax = new Segment(0, 0);

            long number = 0;

            while (number < floor) {
                number++;
                long maxOfMax = ceil(currMax.size - 1);
                long minOfMax = floor(currMax.size - 1);
                long maxOfMin = ceil(currMin.size - 1);
                long minOfMin = floor(currMin.size - 1);

                if (maxOfMax == minOfMax) {
                    nextMax.size = maxOfMax;
                    nextMax.num += 2 * currMax.num;
                } else {
                    nextMax.size = maxOfMax;
                    nextMin.size = minOfMax;
                    nextMax.num += currMax.num;
                    nextMin.num += currMax.num;
                }

                if (currMin.num > 0)
                    if (maxOfMin == minOfMin) {
                        nextMin.size = maxOfMin;
                        nextMin.num += 2 * currMin.num;
                    } else {
                        nextMin.size = minOfMin;
                        nextMax.num += currMin.num;
                        nextMin.num += currMin.num;
                    }

                currMax = nextMax;
                currMin = nextMin;

                nextMax = new Segment(0, 0);
                nextMin = new Segment(0, 0);
            }

            if (currMax.num >= indexOfFloor) {
                max = ceil(currMax.size - 1);
                min = floor(currMax.size - 1);
            } else {
                max = ceil(currMin.size - 1);
                min = floor(currMin.size - 1);
            }

            System.out.printf("Case #%d: %d %d\n", i, max, min);

        }
    }

    public static void main(String[] args) {
        solution();
    }
}

class Segment {
    long size;
    long num;

    public Segment(long size, long num) {
        this.num = num;
        this.size = size;
    }
}
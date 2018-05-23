import java.util.Scanner;

/**
 * @author baiqiang
 *
 */
public class show {
    static Scanner in = new Scanner(System.in);
    
    /*
     * Rounded up.
     */
    static long ceil(long n) {
        return (n >> 1) + (n & 0x1);
    }
    
    /*
     * Rounded down.
     */
    static long floor(long n) {
        return n >> 1;
    }
    
    static void solution() {
        int T = 0;
        T = in.nextInt();
        for(int i = 1; i <= T; i++) {
            long N = in.nextLong();
            long K = in.nextLong();
            
            long min = 0;
            long max = 0;
 
            // <size, num>
//            Map<Long, Integer> currFloor = new HashMap<>();
//            Map<Long, Integer> 
            
            Segment currMin = new Segment(0, 0);
            Segment currMax = new Segment(N, 1);
            
            Segment nextMin = new Segment(0, 0);
            Segment nextMax = new Segment(0, 0);
            
            long j = 0;
            while(j != K) {
                if(currMax.num != 0) {
                    currMax.num--;
                    min = floor(currMax.size - 1);
                    max = ceil(currMax.size - 1);
                    
                    if(min == max) {
                        if(max == nextMax.size)
                            nextMax.num += 2;
                        else if(max == nextMin.size)
                            nextMin.num += 2;
                        else {
                            nextMax.size = max;
                            nextMax.num += 2;
                        }
                    }
                    else {
                        nextMax.size = max;
                        nextMax.num++;
                        nextMin.size = min;
                        nextMin.num++;
                    }
                    j++;
                    
                }
                else if(currMin.num != 0) {
                    currMin.num--;
                    
                    min = floor(currMin.size - 1);
                    max = ceil(currMin.size - 1);
                    
                    if(min == max) {
                        if(max == nextMax.size)
                            nextMax.num += 2;
                        else if(max == nextMin.size)
                            nextMin.num += 2;
                        else {
                            nextMin.size = max;
                            nextMin.num += 2;
                        }
                    }
                    else {
                        nextMax.size = max;
                        nextMax.num++;
                        nextMin.size = min;
                        nextMin.num++;
                    }
                    j++;
                    
                }
                else {
                    currMax = nextMax;
                    currMin = nextMin;
                    nextMax = new Segment(0, 0);
                    nextMin = new Segment(0, 0);
                }
            }
            
            System.out.printf("Case #%d: %d %d\n", i, max, min);
            
        }
    }
    
    public static void main(String[] args) {
        solution();
    }
}

class Segment{
    long size;
    long num;
    
    public Segment(long size, long num) {
        this.num = num;
        this.size = size;
    }
}
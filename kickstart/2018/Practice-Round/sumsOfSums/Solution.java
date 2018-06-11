import java.util.Arrays;
import java.util.Scanner;

class Solution {

    private long getSumUntil(long[] nums, long[] counts, long[] preSums, long a) {
        int pos = Arrays.binarySearch(counts, a);
        if (pos >= 0) {
            return preSums[pos];
        }
        int ip = -pos-1;
        //System.out.println(a + " " + ip + " " + preSums[ip-1] + " " + counts[ip-1] + " " + nums[ip]);
        return preSums[ip-1] + (a-counts[ip-1]) * nums[ip];
    }

    public void solve(long[] v, long[] l, long[] r) {
        int total = 0;
        for (int i = 0; i < v.length; i++){
            total += v[i];
        }
        long[] sums = new long[total+1];
        for (int i = 0; i < v.length; i++) {
            total = 0;
            for (int j = i; j < v.length; j++) {
                total += v[j];
                sums[total]++;
            }
        }
        int nonzeros = 0;
        for (int i = 0; i < sums.length; i++) {
            //System.out.println(i + " " + sums[i]);
            if (sums[i] != 0) {
                nonzeros++;
            }
        }
        //System.out.println(nonzeros);
        long[] nums = new long[nonzeros+1];
        long[] counts = new long[nonzeros+1];
        long[] preSums = new long[nonzeros+1];
        int index = 0;
        for (int i = 1; i < sums.length; i++) {
            if (sums[i] != 0) {
                index++;
                nums[index] = i;
                counts[index] = counts[index-1] + sums[i];
                preSums[index] = preSums[index-1] + sums[i] * i;
                //System.out.println(nums[index] + " " + counts[index] + " " + preSums[index]);
            }
        }
        for (int i = 0; i < l.length; i++) {
            System.out.println(getSumUntil(nums, counts, preSums, r[i]) - getSumUntil(nums, counts, preSums, l[i]-1));
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int cs = 1; cs <= T; cs++) {
            System.out.println("Case #" + cs + ":");
            int N, Q;
            N = sc.nextInt();
            Q = sc.nextInt();
            long[] v = new long[N];
            for (int i = 0; i < N; i++) {
                v[i] = sc.nextLong();
            }
            long[] l = new long[Q];
            long[] r = new long[Q];
            for (int i = 0; i < Q; i++) {
                l[i] = sc.nextLong();
                r[i] = sc.nextLong();
            }
            sol.solve(v, l, r);
        }
    }
}
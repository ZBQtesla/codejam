import java.util.Arrays;

/**
 * @author baiqiang
 */

public class Solution {
  private static final double E = 0.000001;

  /**
   * Find the median of two sorted arrays.
   */
  public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    int m = nums1.length;
    int n = nums2.length;
    if(m == 0 && n != 0){
      return getMedian(nums2);
    }
    if(m != 0 && n == 0){
      return getMedian(nums1);
    }
    if(m == 0 && n == 0){
      return 0;
    }
    double median1 = getMedian(nums1);
    double median2 = getMedian(nums2);

    // Termination condition
    if (Math.abs(median1 - median2) < E) {
      return median1;
    }

    if (m == 1 || n == 1) {
      if(m == 1 && n == 1){
        return (nums1[0] + nums2[0]) / 2.0;
      }
      int single = 0;
      int[] num = null;
      if (m == 1) {
        single = nums1[0];
        num = nums2;
      } else {
        single = nums2[0];
        num = nums1;
      }
      int len = num.length;
      num = Arrays.copyOfRange(num, (len / 2) - 1, (len / 2) + 1 + (len % 2));
      int index = num.length;
      len = num.length;
      for (int i = 0; i < len; i++) {
        if (num[i] > single) {
          index = i;
          break;
        }
      }
      int[] result = new int[len + 1];
      for (int i = 0; i < index; i++) {
        result[i] = num[i];
      }
      result[index] = single;
      if(index != len){
        for (int i = index + 1; i < len + 1; i++) {
          result[i] = num[i - 1];
        }
      }
      return getMedian(result);
    }

    // Divide
    int minSize = m < n ? m / 2 : n / 2;
    return median1 < median2
        ? findMedianSortedArrays(Arrays.copyOfRange(nums1, minSize, m),
            Arrays.copyOfRange(nums2, 0, n - minSize))
        : findMedianSortedArrays(Arrays.copyOfRange(nums1, 0, m - minSize),
            Arrays.copyOfRange(nums2, minSize, n));
  }

  /**
   * Get a array's median.
   */
  public double getMedian(int[] nums) {
    int n = nums.length;
    return (double) (nums[n / 2] + nums[(n - 1) / 2]) / 2.0;
  }

  public static void main(String[] args) {
    int[] nums1 = {1, 2};
    int[] nums2 = {3, 4};
    Solution s = new Solution();
    System.out.println(s.findMedianSortedArrays(nums1, nums2));
  }
}

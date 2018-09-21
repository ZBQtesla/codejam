import java.util.*;
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

    // Base case
    if(m <= 2 || n <= 2){
      if(m > 2){
        nums1 = Arrays.copyOfRange(nums1, (m - 3) / 2, (m + 4) / 2);
      }
      if(n > 2){
        nums2 = Arrays.copyOfRange(nums2, (n - 3) / 2, (n + 4) / 2);
      }
      List<Integer> result = new ArrayList<>();
      for(int e : nums1){
        result.add(e);
      }
      for(int e : nums2){
        result.add(e);
      }
      Collections.sort(result);
      return (result.get(result.size() / 2) + result.get((result.size() - 1) / 2)) / 2.0;
    }

    double median1 = getMedian(nums1);
    double median2 = getMedian(nums2);
    if(Math.abs(median1 - median2) < E){
      return median1;
    }

    // Divide
    int minSize = m < n ? (m - 1) / 2 : (n - 1) / 2;
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

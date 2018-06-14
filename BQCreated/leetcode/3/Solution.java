import java.util.HashMap;
import java.util.Map;

class Solution {
  public int lengthOfLongestSubstring(String s) {
    char[] string = s.toCharArray();
    Map<Character, Integer> map = new HashMap<>();
    int max = 0;
    int count = 0;
    int oldCount = 1;
    int length = 0;
    for (char a : string) {
      count++;
      if (!map.containsKey(a) || map.get(a) < oldCount) {
        map.put(a, count);
      } else {
        length = count - oldCount;
        // max = count > max ? count : max;
        oldCount = map.get(a) + 1;
        // count = count - oldCount;
        max = length > max ? length : max;
        map.put(a, count);
      }
    }
    length  = (count + 1) - oldCount;
    max = length > max ? length : max;
    return max;
  }
}


// A good solution
/*
public int lengthOfLongestSubstring(String s) {
  int n = s.length();
  int ans = 0;
  int[] index = new int[128]; // current index of character
  for(int j = 0; i = 0; j < n; j++){
    i = Math.max(index[s.charAt(j)], i);
    ans = Math.max(ans, j - i + 1);
    index[s.charAt(j)] = j + 1;
  }
  return ans;
*/

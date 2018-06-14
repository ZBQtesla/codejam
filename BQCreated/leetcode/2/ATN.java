/**
 * 总结：
 * 注意java中没有指针的概念
 * 所以保留链表头的时候，必须要先new一个对象
 */
 
  /**
   * Definition for singly-linked list.
   * public class ListNode {
   *     int val;
   *     ListNode next;
   *     ListNode(int x) { val = x; }
   * }
   */
  class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
      ListNode p = new ListNode(0);
      ListNode result = p;
      if(l1 == null && l2 == null)
        return null;
      int carry = 0;
      do{
        int val = l1.val + l2.val + carry;
        l1 = l1.next;
        l2 = l2.next;
        carry = val / 10;
        p.val = val %10;
        if(l1 != null && l2 != null){
          p.next = new ListNode(0);
          p = p.next;
        }
      }while(l1 != null && l2 != null);

      while(l1 != null){
        int  val = l1.val + carry;
        l1 = l1.next;
        p.next = new ListNode(val % 10);
        carry = val / 10;
        p = p.next;
      }
      while(l2 != null){
        int  val = l2.val + carry;
        l2 = l2.next;
        p.next = new ListNode(val % 10);
        carry = val / 10;
        p = p.next;
      }
      if(carry != 0){
        p.next = new ListNode(carry);
      }
      return result;
    }
  }

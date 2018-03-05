/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    int c;
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        LinkedList<ListNode> l = new LinkedList<>();
        int a;
        while(l1 != null|| l2 != null){
            int w = 0,e = 0;
            if(l1 != null)w = l1.val;
            if(l2 != null)e = l2.val;
            if(l1 == null){w = 0;}
            if(l2 == null){e = 0;}
           int[] q = addition(w, e);
           a = q[0];
           if(c == 0){
               ListNode a0 = new ListNode(a);
               l.add(a0);
           }
            else{
               ListNode a0 = new ListNode(a);
               l.add(a0);
             }
            if(l1 != null)l1 = l1.next;
            if(l2 != null)l2 = l2.next;
        }
        if(c == 1) l.add(new ListNode(1));
        for(int i = 0; i < l.size() - 1; i++){
            l.get(i).next = l.get(i + 1);
        }
        return l.getFirst();
    }
    public int[] addition(int a, int b){
        int r[] = new int[2];
        if(a + b + c < 10){
            r[0] = a + b + c;
            c = 0;
            return r;
        }
        else{
            r[0] = a + b + c - 10;
            c = 1;
            return r;
        }    
    }
}

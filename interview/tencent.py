# 最小硬币数面值：[x1,x2,x3,…]总面值：m求构成m的最小硬币数（每个面值的硬币可以无限个）Eg. [1,3,5] m=10, 最小硬币数为2




# 编程题链表相加input: (2 -> 4 -> 3) + (5 -> 6 -> 4) Output: 7 -> 0 -> 8 Explanation: 342 + 465 = 807
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 
# @param l1 ListNode类 
# @param l2 ListNode类 
# @return ListNode类
#
class Solution:
    def addTwoNumbers(self , l1 , l2 ):
        # write code here
        result = ListNode(-1);
        pre = result
        carry=0
        
        while l1!=None or l2!=None:
            d1 = 0 if l1==None else l1.val
            d2 = 0 if l2==None else l2.val
            sum = d1 + d2 + carry
            carry = 1 if sum>= 10 else 0
            pre.next = ListNode(sum%10)
            pre=pre.next
            l1 = l1.next if l1.next!=None else None
            l2 = l2.next if l2.next!=None else None

        if carry==1:
            pre.next = ListNode(carry)

        return result.next
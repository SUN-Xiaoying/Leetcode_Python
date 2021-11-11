# 如何判断两个有环单链表是否相交？相交的话返回第一个相交的节点，不想交的话返回空。如果两个链表长度分别为N和M，请做到时间复杂度O(N+M)，额外空间复杂度O(1)。

# 给定两个链表的头结点head1和head2(注意，另外两个参数adjust0和adjust1用于调整数据,与本题求解无关)。请返回一个bool值代表它们是否相交。


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ChkIntersection:

    def chkInter(self, head1, head2, adjust0, adjust1):
        # write code here
        def getLoopNode(pHead):
            if not pHead or not pHead.next or not pHead.next.next:
                return None
            slow,fast=pHead.next, pHead.next.next
            while slow!=fast:
                slow=slow.next
                fast=fast.next.next
            fast=pHead
            while slow!=fast:
                slow=slow.next
                fast=fast.next
            return slow 

        loop1=getLoopNode(head1)
        loop2=getLoopNode(head2)

        if loop1==loop2: return True
        else:
            p=loop1.next
            while p!=loop1:
                if (p==loop2): return True
                p=p.next
                
        return False
            
            
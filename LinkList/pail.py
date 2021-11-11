# 回文结构
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self, data):
        newNode = ListNode(data)
        if(self.head):
            current = self.head
            while(current.next):
                current=current.next
            current.next=newNode
        else:
            self.head=newNode

    def printLL(self):
        current=self.head
        s=""
        while(current):
            s.join(" -> ", current.val)
            current = current.next

        print(s)

class Solution:
    def isPail(self , head: ListNode) -> bool:
        # write code here
        if head is None:
            return False

        slow, fast= head, head
        while fast and fast.next:
            print(slow.val, fast.val)
            slow=slow.next
            fast=fast.next.next
        
        rever_head = slow
        pre = None

        while rever_head:
            tmp=rever_head.next
            rever_head.next=pre
            pre=rever_head
            rever_head=tmp

        while pre:
            if(head.val != pre.val):
                return False
            pre=pre.next
            head=head.next

        return True

s=Solution()
LL = LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(2)
LL.insert(1)
LL.insert(3)

print(s.isPail(LL.head))
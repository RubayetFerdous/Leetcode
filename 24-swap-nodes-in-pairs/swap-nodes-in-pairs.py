# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def count(self, head, x=0):
        if not head: return x
        return self.count(head.next,x+1)
        
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        c= self.count(head)

        if c<2:return head
        
        if not head.next: return node

        node=ListNode(head.next.val,ListNode(head.val))
        node.next.next= self.swapPairs(head.next.next)

        return node



        




        


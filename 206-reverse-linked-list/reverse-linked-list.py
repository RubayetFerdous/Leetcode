# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def new(self,head):
        if not head: return None, None
        new_head, tail = self.new(head.next)
        new_node= ListNode(head.val)
        if not tail: return new_node, new_node
        else:
            tail.next=new_node
            return new_head, new_node

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node,_=self.new(head)
        return node

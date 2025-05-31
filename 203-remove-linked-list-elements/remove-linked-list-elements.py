# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if not head: return head

        node= ListNode(head.val)

        node.next= self.removeElements(head.next,val)

        if node.val==val: return node.next

        return node
        
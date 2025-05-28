# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:

        front=head

        def recurse(tail):

            nonlocal front

            if not tail: return True
            if not recurse(tail.next): return False
            if front==tail or front.next==tail:
                tail.next=None
                return False

            new=front.next
            front.next=tail
            tail.next=new
            front=new

            return True
        
        recurse(head)


            



        




        
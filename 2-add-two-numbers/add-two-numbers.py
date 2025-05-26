# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def count(self,head, x = 0):

        if head == None: return x

        return self.count(head.next, x+1)

    def summation(self,h1, h2, carry):

        if not h1: return None if carry==0 else ListNode(carry)

        if h2: val2= h2.val
        else: val2= 0

        val1= h1.val

        total= val1 + val2 + carry
        carry= total // 10


        node= ListNode(total % 10)

        node.next= self.summation(h1.next, h2.next if h2 else None, carry)

        return node


        



    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        c1, c2=self.count(l1), self.count(l2)

        if c1> c2: h1, h2=l1, l2
        else: h1, h2=l2, l1

        return self.summation(h1, h2, 0)
        

        
        
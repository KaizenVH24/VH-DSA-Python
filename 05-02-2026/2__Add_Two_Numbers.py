# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # num1 = 0
        # num2 = 0
        # place = 1

        # while l1:
        #     num1 += l1.val * place
        #     place *= 10
        #     l1 = l1.next

        # place = 1
        # while l2:
        #     num2 += l2.val * place
        #     place *= 10
        #     l2 = l2.next
        
        # total = num1 + num2
        # if total == 0:
        #     return ListNode(0)

        # dummy = ListNode(0)
        # curr = dummy

        # while total > 0:
        #     curr.next = ListNode(total % 10)
        #     total //= 10
        #     curr = curr.next
        
        # return dummy.next

        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            curr.next = ListNode(total%10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next
            
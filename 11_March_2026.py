# 19. Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # length = 0
        # curr = head
        
        # while curr:
        #     length += 1
        #     curr = curr.next
        
        # remove_index = length - n
        
        # if remove_index == 0:
        #     return head.next
        
        # curr = head
        
        # for i in range(remove_index - 1):
        #     curr = curr.next
        
        # curr.next = curr.next.next
        
        # return head

        dummy = ListNode(0)
        dummy.next = head
        
        fast = dummy
        slow = dummy
        
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return dummy.next

# 20. Valid Parenthesis
  class Solution:
    def isValid(self, s: str) -> bool:
        
        # while "()" in s or "{}" in s or "[]" in s:
        #     s = s.replace("()", "")
        #     s = s.replace("{}", "")
        #     s = s.replace("[]", "")
        
        # return s == ""

        stack = []
        
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        
        return not stack

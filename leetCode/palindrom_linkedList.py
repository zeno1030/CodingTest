class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []

        if not head:
            return True

        while head is not None:
            stack.append(head.val)
            head = head.next

        while len(stack) > 1:
            if stack.pop(0) != stack.pop():
                return False
        return True
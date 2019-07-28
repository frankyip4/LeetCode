# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # divmod return a tuple (quotient, remainder)
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        temp = result = ListNode(0)
        while (l1 or l2 or carry == 1):
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            # No need for else statement to update anything
            # else:
            #     val1 = 0
            #     l1 = None
            if l2:
                val2 = l2.val
                l2 = l2.next
            # else:
            #     val2 = 0
            #     l2 = None
            carry, num = divmod(val1 + val2 + carry, 10)
            temp.next = ListNode(num)
            temp = temp.next
        return result.next

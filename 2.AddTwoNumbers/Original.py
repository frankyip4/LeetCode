# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import math

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        num2 = 0
        count = 0
        num = 0
        if(l1):
            num = l1.val
        if(l2):
            num += l2.val
        if num >= 10:
            carry = 1
            num -= 10
        else:
            carry = 0
        result = ListNode(num)
        temp = result
        while not(l1.next == None or l2.next == None):
            num = l1.next.val + l2.next.val + carry
            carry = 0
            if num >= 10:
                carry = 1
                num -= 10
            temp.next = ListNode(num)
            l1 = l1.next
            l2 = l2.next
            temp = temp.next
        if l1.next:
            while l1.next:
                num = l1.next.val + carry
                carry = 0
                if num >= 10:
                    carry = 1
                    num -= 10
                temp.next = ListNode(num)
                l1 = l1.next
                temp = temp.next
        elif l2.next:
            while l2.next:
                num = l2.next.val + carry
                carry = 0
                if num >= 10:
                    carry = 1
                    num -= 10
                temp.next = ListNode(num)
                l2 = l2.next
                temp = temp.next
        if carry == 1:
            temp.next = ListNode(1)
        return result

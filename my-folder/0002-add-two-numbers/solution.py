# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        current = dummyNode
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)

            carry, out =divmod(val1 + val2 + carry, 10)

            current.next = ListNode(out)
            current = current.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        
        return dummyNode.next

    def to_linked_list(nums):
        dummyNode = ListNode()
        current = dummyNode
        for num in nums:
            current.next = ListNode(num)
            current = current.next
        return dummyNode.next
    
    def to_list(node):
        reulst = []
        while node:
            result.append(node.val)
            node = node.next
        return result
        


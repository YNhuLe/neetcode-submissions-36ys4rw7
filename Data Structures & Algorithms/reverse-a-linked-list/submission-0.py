# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       #need 2 pointers
       #prev point to NUll
       #head is curr pointer
       #temp pointer will keep the chain when changing the pointer to point to the previous node
        prev = None
        curr = head

        while curr:
            temp = curr.next #temp pointer to keep chain from the current node to the next node
            curr.next = prev # curr pointer move backward
            prev = curr #prev pointer will move forward by 1 node
            curr = temp
        return prev
    


        
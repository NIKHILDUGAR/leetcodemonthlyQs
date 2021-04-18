#MY WAY . NOT GOOD
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        arr=[]
        curr=head
        while (curr != None): 
            arr.append(curr.val)
            curr = curr.next
        k=len(arr)-n
        arr=(arr[:k]+arr[k+1:])
        def insert(root, item):
            temp = ListNode(item)
            if (root == None):
                root = temp
            else :
                ptr = root
                while (ptr.next != None):
                    ptr = ptr.next
                ptr.next = temp
            return root
        root = None
        for i in arr:
            root = insert(root,i)
        return root

      
      
#BETTER WAY

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    dummy = new_head = ListNode(-1, head)
    fast = slow = dummy
    for _ in range(n):
      fast = fast.next
    
    while fast and fast.next:
      slow = slow.next
      fast = fast.next
    
    slow.next = slow.next.next
    return new_head.next

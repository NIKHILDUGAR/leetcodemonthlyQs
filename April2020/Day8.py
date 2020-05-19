# question link - https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3290/
class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

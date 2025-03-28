
# 2. Add Two Numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        carry = 0
        first = True

        while l1 or l2:
            if first:
                curr = res
                first = False
            else:
                curr.next = ListNode()
                curr = curr.next

            if l1 and l2:
                curr.val = (l1.val + l2.val + carry) % 10
                carry = (l1.val + l2.val + carry) // 10
                l1 = l1.next
                l2 = l2.next
            elif l1:
                curr.val = (l1.val + carry) % 10
                carry = (l1.val + carry) // 10
                l1 = l1.next
            elif l2:
                curr.val = (l2.val + carry) % 10
                carry = (l2.val + carry) // 10
                l2 = l2.next
            print(carry)

        if carry:
            curr.next = ListNode()
            curr.next.val = carry

        return res

#3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        count = 0
        max = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] in st:
                    max = max if max >= count else count
                    count = 0
                    st.clear()
                    break
                
                st.add(s[j])
                count += 1
        
        return max if max >= count else count
    
#3. Longest Substring Without Repeating Characters(with sliding window approach)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        max = 0
        l = 0
        r = 0
        
        while r < len(s):
            if s[r] in st:
                while True:
                    st.remove(s[l])
                    l += 1

                    if s[r] not in st:
                        break

            st.add(s[r])
            r += 1
            max = max if max >= len(st) else len(st)
        
        return max if max >= len(st) else len(st)
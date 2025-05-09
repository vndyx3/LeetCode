#4. Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = 0
        l2 = 0
        r1 = len(nums1) - 1
        r2 = len(nums2) - 1
        len1 = len(nums1)
        len2 = len(nums2)
        nums_left = len(nums1) + len(nums2)
        even = nums_left % 2 == 0

        if not len1 and not len2:
            return 0

        while True:
            if even and nums_left == 2:
                if l1 < r1:
                    return (nums1[l1] + nums1[r1]) / 2
                elif l2 < r2:
                    return (nums2[l2] + nums2[r2]) / 2
                else:
                    return (nums1[l1] + nums2[l2]) / 2
            elif not even and nums_left == 1:
                return nums1[l1] if l1 == r1 else nums2[l2]

            if l1 <= r1 and (l2 > r2 or nums1[l1] <= nums2[l2]):
                l1 += 1
            else:
                l2 += 1
            
            if l1 <= r1 and (l2 > r2 or nums1[r1] >= nums2[r2]):
                r1 -= 1
            else:
                r2 -= 1
 
            nums_left -= 2

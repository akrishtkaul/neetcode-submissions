class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        l = 0
        r = 0

        while r < n and l < m:

            if( nums1[l] > nums2[r] ):
                nums1.insert(l, nums2[r])
                nums1.pop()
                r += 1
                m += 1

            l += 1


        if m != len(nums1):
            for i in range(m, len(nums1)):
                nums1[i] = nums2[r]
                r += 1
        
        
        
        

        
        
        
        
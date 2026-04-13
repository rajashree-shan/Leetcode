class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        hm={}
        for num in nums2:
            while stack and num>stack[-1]:
                hm[stack.pop()]=num
            stack.append(num)
        while stack:
            hm[stack.pop()]= -1
        return [hm[x] for x in nums1]
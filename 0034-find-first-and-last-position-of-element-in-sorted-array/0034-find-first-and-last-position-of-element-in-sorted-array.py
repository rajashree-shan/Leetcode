class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums,target):
            left=0
            right=len(nums)-1
            first=-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]<target:
                    left=mid+1
                elif nums[mid]>target:
                    right=mid-1
                else:
                    first=mid
                    right=mid-1
            return first
        def find_last(nums,target):
            left=0
            right=len(nums)-1
            last=-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]<target:
                    left=mid+1
                elif nums[mid]>target:
                    right=mid-1
                else:
                    last=mid
                    left=mid+1
            return last
        first = find_first(nums, target)
        if first == -1:
            return [-1, -1]

        last = find_last(nums, target)
        return [first, last]



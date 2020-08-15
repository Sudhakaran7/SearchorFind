class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)

val=Solution()
n,target=map(int,input().split())
nums=list(map(int,input().split()))
print(val.searchInsert(nums,target))

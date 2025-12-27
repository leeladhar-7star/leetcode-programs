 class Solution:
     def moveZeroes(self, nums):
        """
        do not return anything, modify nums in-place
        """
        idx = 0
        for i in range (len(nums)):
            if nums[i]!=0:
                nums[idx]=nums[i]
                idx+=1
        for i in range(idx,len(nums)):
            nums[i]=0

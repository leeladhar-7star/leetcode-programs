class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k% len(nums)
        '''nums[:]=nums[-k:]+nums[:-k]'''
        def reve(L,r):
            while L<r:
                nums[L],nums[r]=nums[r],nums[L]
                L+=1
                r-=1
        reve(0,len(nums)-1)
        reve(0,k-1)
        reve(k,len(nums)-1)
        
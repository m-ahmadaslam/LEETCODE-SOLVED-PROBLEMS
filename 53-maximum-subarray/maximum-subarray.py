class Solution(object):
    def maxSubArray(self, nums):
        total = 0
        res=nums[0]


        for n in nums:
            if total < 0:
                total=0

            total+=n

            res=max(res,total)

        return res
          
        
class Solution(object):
    def findMaxLength(self, nums):
        prefix_sum_map ={0:-1}
        max_sum=0
        prefix_sum=0

        for i,num in enumerate(nums):
            if num==0:
                prefix_sum -=1

            else:
                prefix_sum += 1

            
            if prefix_sum in prefix_sum_map:
                max_sum = max(max_sum, i - prefix_sum_map       [prefix_sum])

            else:
                prefix_sum_map[prefix_sum] = i

        return max_sum



        
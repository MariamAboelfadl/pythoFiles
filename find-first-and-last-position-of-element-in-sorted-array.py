class Solution(object):
    def searchRange(self, nums, target):
       if target not in nums :
            return [-1, -1]
       elif len(nums) == 1 :
            return [0, 0]
       for i in range(len(nums)):
           if nums[i] == target:
               for j in range(i,len(nums)):
                   if nums[j] != target:
                       break
               if j == len(nums)-1:
                   if nums[j] == target:
                       return [i,j]
               return [i,j-1]
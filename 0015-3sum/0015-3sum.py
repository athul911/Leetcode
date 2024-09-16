class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        #[-4,-1,-1,0,1,2]
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:
                total = nums[i] + nums[left]+ nums[right]
                if  total == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left] == nums[left+1]:
                        left+=1
                    while left<right and nums[right] == nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif total > 0:
                    right-=1
                else :
                    left+=1

        return res
                
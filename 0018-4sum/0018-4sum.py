class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left = j + 1
                right = len(nums)-1
                while left<right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        item = [nums[i] , nums[j] , nums[left] , nums[right]]
                        if item not in res:
                            res.append(item)
                        while left<right and nums[left] == nums[left+1]:
                            left+=1
                        while left<right and nums[right] == nums[right-1]:
                            right-=1
                        left+=1
                        right-=1
                    elif total<target:
                        left+=1
                    else:
                        right-=1

        return res
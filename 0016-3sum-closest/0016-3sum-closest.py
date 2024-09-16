class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1

            while left<right:
                total = nums[i] + nums[left] + nums [right]
                diff = abs(total - target)
                if diff < abs(res-target):
                    res = total
                
                if total > target:
                    right-=1
                elif total < target:
                    left+=1
                else:
                    return total
        return res
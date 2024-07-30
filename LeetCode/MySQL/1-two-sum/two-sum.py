class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Exhaustive Search
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        # Two Pointers
        new_nums = [[v, i] for i, v in enumerate(nums)]
        new_nums.sort(key=lambda x:x[0])
        
        l, r = 0, len(nums)-1
        while l < r:
            nums_sum = new_nums[l][0] + new_nums[r][0]
            if nums_sum > target:
                r -= 1
            elif nums_sum < target:
                l += 1
            else:
                return [new_nums[l][1], new_nums[r][1]]
        



        

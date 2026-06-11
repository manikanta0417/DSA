class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        j = 0

        while j <= len(nums) - 1:
            if nums[j] != 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
            j += 1

        return nums
        
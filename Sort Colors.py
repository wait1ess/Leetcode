class Solution():
    def sortColors(self, nums):
        left = mid = 0
        right = len(nums) - 1
        while mid <= right:
            if nums[mid] == 0:
                nums[mid], nums[left] = nums[left], nums[mid]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1


if __name__=="__main__":
    nums=[2,2]
    Solution().sortColors(nums)
    print(nums)

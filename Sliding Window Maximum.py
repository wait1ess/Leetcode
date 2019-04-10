class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        # window 固定大小的滑动窗口，但小于新加入元素的前面的元素出窗
        window,res=[],[]
        for index,element in enumerate(nums):
            if index>=k and window[0]<=index-k:
                window.pop(0)
            while window and nums[window[-1]]<=element:
                window.pop()
            window.append(index)
            if index>=k-1:
                res.append(nums[window[0]])
        return res

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(1, len(nums)):
            if nums[cnt] != nums[i]:
                cnt += 1
                nums[cnt] = nums[i]
        return cnt + 1
    
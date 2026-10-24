class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left != right:
            index = (left + right) // 2
            if (nums[index] == target):
                return index
            elif (nums[index] < target):
                left = index + 1
            else:
                right = index

        return -1
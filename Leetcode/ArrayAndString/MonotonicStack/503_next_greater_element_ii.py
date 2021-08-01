class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums = nums + nums

        res = [-1 for _ in range(len(nums))]
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                cur_idx = stack.pop()
                res[cur_idx] = nums[i]
            stack.append(i)

        return res[:len(nums) // 2]


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1 for _ in range(len(nums))]
        stack = []
        for i in range(len(nums) * 2 - 1):
            while stack and nums[i % len(nums)] > nums[stack[-1]]:
                cur_idx = stack.pop()
                res[cur_idx] = nums[i % len(nums)]
            stack.append(i % len(nums))

        return res
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        res = [-1 for _ in range(n)]
        res_map = {}

        for i, num in enumerate(nums1):
            res_map[num] = i
        
        stack = []

        # print (res_map)
        for i in range(len(nums2)):
            cur_val = nums2[i]
            while stack and nums2[stack[-1]] < cur_val:
                popIdx = stack.pop()
                if nums2[popIdx] in res_map:
                    res[res_map[nums2[popIdx]]] = cur_val‵
            stack.append(i)

        return res




class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res_dict = {i:-1 for i in nums2}
        for i in nums2:
            while stack and i > stack[-1]:
                small = stack.pop()
                res_dict[small] = i
            stack.append(i)
        res = []
        for j in nums1:
            res.append(res_dict[j])
        return res

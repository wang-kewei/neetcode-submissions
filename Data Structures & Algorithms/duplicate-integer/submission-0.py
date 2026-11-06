class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elem = {}
        for i in nums:
            if i in elem:
                return True
            elem[i] = 1
        return False
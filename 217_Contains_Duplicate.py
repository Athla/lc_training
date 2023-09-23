class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ran = set()
        for i in nums:
            if i in ran:
                return True
            ran.add(i)
        return False


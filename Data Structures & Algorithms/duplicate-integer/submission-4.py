class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_duplicate = {}
        for i in nums:
            if i in count_duplicate:
                return True
            else:
                count_duplicate[i] = 1;

        return False;
        
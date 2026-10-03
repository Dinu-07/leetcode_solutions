class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        i = len(candyType)//2
        set_ = set(candyType)
        if len(set_) > i:
            return i
        else:
            return len(set_)
        
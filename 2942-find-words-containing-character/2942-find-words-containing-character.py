class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        list_ = []
        for i in range(len(words)):
            if x in words[i]:
                list_.append(i)
        return list_

        
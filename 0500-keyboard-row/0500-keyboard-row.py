class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_row = 0
        second_row = 0
        third_row = 0
        list_ = []

        for i in words:
            for j in i:
                if j in "qwertyuiop" or j in "QWERTYUIOP":
                    first_row+=1
                elif j in "asdfghjkl" or j in "ASDFGHJKL":
                     second_row+=1
                elif j in "zxcvbnm" or j in "ZXCVBNM":
                    third_row+=1
                else:
                    pass
            if first_row == len(i) or second_row == len(i) or third_row == len(i):
                list_.append(i)
            first_row = 0
            second_row = 0
            third_row = 0
        return list_


        
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        i = len(num1)-1
        j = len(num2)-1
        carry=0
        while i>=0 or j>=0 or carry:
            if i>=0:
                digit1 = ord(num1[i]) - ord('0')
            else:
                digit1 = 0
            if j>=0:
                digit2 = ord(num2[j]) - ord('0')
            else:
                digit2 = 0
            total = digit1 + digit2+carry
            carry = total // 10
            total = chr(total %10 + ord('0'))
           
            result.append(total)
            i-=1
            j-=1
        return "".join(reversed(result))
import sys


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ret = []
        carry = 0
        for i in reversed(range(len(digits))):

            digit = int(digits[i]) + carry
            if i == len(digits) - 1:
                digit += 1

            if digit > 9:
                digit = 0
                carry = 1
            else:
                carry = 0

            ret.append(digit)

        if carry:
            ret.append(1)

        ret.reverse()
        return ret


if __name__ == '__main__':
    print(Solution().plusOne(sys.argv.copy()[1:]))

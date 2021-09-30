

class Solution:

    @staticmethod
    def longest_palindromic(s: str) -> str:
        def longest_palindromic(s: str) -> str:
        res = ""

        if len(s) == 1:
            print(s)
        else:
            for v in range(1, len(s)):
                if s == s[::-1]:
                    if len(s) >= len(res):
                        res = s
                    break
                else:
                    for i in range(1, len(s)):
                        subString = s[i:]
                        if subString == subString[::-1]:
                            if len(subString) >= len(res):
                                res = subString
                            break
                s = s[:-v]
        print(res)
Solution.longest_palindromic(s="babad")

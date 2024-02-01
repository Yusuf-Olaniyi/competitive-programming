class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strings = sorted(strs, key=lambda x: len(x))
        string = ''
        for i in range(len(strings[0])):
            letter = True
            for j in strings[1:]:
                if j[i] != strings[0][i]:
                    return string

            if letter:
                string += strings[0][i]
        return string

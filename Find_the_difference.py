class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        def get_count(string):
            value_counts = Counter(string)

            result_dict = dict(value_counts)

            return result_dict
        s_dict = get_count(s)
        t_dict = get_count(t)
        for i in t_dict:
            if i not in s_dict:
                return i
            elif  s_dict[i] != t_dict[i]:
                return i
        

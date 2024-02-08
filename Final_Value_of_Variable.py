class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = 0
        for i in operations:
            desc = ''.join(sorted(set(i))) 
            if desc == '+X':
                value += 1
            elif desc == '-X':
                value -= 1
        return value

        

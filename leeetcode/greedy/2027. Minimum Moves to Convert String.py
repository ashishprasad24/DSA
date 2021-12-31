class Solution:
    def minimumMoves(self, s: str) -> int:
        i = 0
        ops = 0
        while i < len(s):
            if s[i] == 'X':
                ops += 1
                i += 3
            else:
                i += 1    
        return ops

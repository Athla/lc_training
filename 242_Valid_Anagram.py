def isAnagram(self, s: str, t: str) -> bool:
        """
        Solution 1: Using sorting methods
        """
        s_sorted = sorted(s)
        t_sorted = sorted(t)

        if s_sorted == t_sorted:
            return True
        return False

def isAnagram_2(self, s: str, t: str) -> bool:
        """
        
        Solution 2: Using list sorting. it faster, same memory consumption"""
        s_sorted = [ls for ls in s]
        s_sorted.sort()
        t_sorted = [ts for ts in t]
        t_sorted.sort()

        if s_sorted == t_sorted:
            return True
        return False

class solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = joint(sorted(s))
        t = joint(sorted(t))
        if s == t:
            return True
    else:
        return False
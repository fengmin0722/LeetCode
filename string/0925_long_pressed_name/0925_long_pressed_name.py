class Solution(object):
    def isLongPressedName(self, name, typed):
        i = 0
        for j in xrange(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j-1]:
                return False
        return i == len(name)

    
name = "alexx"
typed = "aaleexxx"

print(Solution().isLongPressedName(name, typed))
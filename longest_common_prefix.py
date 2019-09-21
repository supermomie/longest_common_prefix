class prefix:
    """
    here my first attenpt
    def longestCommonPrefix(self, strs):
        prefix = ""
        for i in range(len(strs)):
            if (list(strs[i])[:2]) == (list(strs[-1])[:2]):
                prefix = ''.join(list(strs[i][:2]))
            else:
                break
        return prefix
    """
    
    def longestCommonPrefix(self, strs):
        prefix = ""
        for i in zip(*[list(i) for i in strs]):
            if len(set(i)) == 1:
                prefix += i[0]
                #print(prefix)
            else:
                break 
        
        return prefix



res = prefix()
print(res.longestCommonPrefix(["flower","flow","flight"]))
print(res.longestCommonPrefix(["dog","racecar","car"]))
print(res.longestCommonPrefix(["aa","ab"]))

class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = {}
        
        for word in strs:
            key = ''.join(sorted(word))
            
            if key not in hashmap:
                hashmap[key] = []
            
            hashmap[key].append(word)
        
        return list(hashmap.values())
        
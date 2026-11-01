class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        map = {}
        
        for st in strs:
            letter = [0] * 26
            
            for ch in st:
                letter[ord(ch) - ord('a')] += 1
            
            key = str(letter)

            if key not in map:
                map[key] = [st]
            else:
                map[key].append(st)
            
        return list(map.values())

            
            
             
                
                
        
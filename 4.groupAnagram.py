class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = {}
        
        for strg in strs:
            sorted_string = ''.join(sorted(strg))

            if sorted_string not in strs_map:
                strs_map[sorted_string] = []
            
            strs_map[sorted_string].append(strg)

        return list(strs_map.values())

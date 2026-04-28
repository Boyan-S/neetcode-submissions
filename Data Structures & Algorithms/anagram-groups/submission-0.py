class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in groups:
                groups[sorted_string] = [string]
            else:
                groups[sorted_string].append(string)
        print(groups)
        return list(groups.values())
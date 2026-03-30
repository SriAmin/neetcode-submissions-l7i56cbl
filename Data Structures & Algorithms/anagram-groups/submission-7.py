class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for string in strs:
            chars = [0] * 26

            for c in string:
                chars[ord(c) - ord('a')] += 1
            output[tuple(chars)].append(string)
        return list(output.values())
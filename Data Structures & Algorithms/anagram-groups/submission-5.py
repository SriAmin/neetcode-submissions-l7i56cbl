class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        for string in strs:
            if len(output) == 0:
                output.append([string])
            else:
                inserted = False
                for anagram in output:
                    ana = anagram[0]
                    if sorted(string) == sorted(ana):
                        anagram.append(string)
                        inserted = True
                        break
                if not inserted:
                    output.append([string])
        return output
class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        length = ""
        i = 0
        while i < len(s):
            if s[i] == "#":
                stringStart = i + 1
                lengthNum = int(length)
                length = ""
                output.append(s[stringStart : stringStart + lengthNum])
                i = stringStart + lengthNum
            else:
                length += s[i]
                i += 1
        return output



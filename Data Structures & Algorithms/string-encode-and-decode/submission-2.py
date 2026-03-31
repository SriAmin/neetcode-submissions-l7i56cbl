class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output += str(len(string)) + "#" + string
        return output

    def decode(self, s: str) -> List[str]:
        if s == "0#":
            return [""]

        length = ""
        lengthNum = 0
        lengthFlag = True
        tempStr = ""
        output = []

        for c in s:
            if lengthFlag:
                if c == "#":
                    lengthNum = int(length)
                    length = ""
                    if lengthNum == 0:
                        output.append("")
                    else:
                        lengthFlag = False
                else:
                    length += c
            else:
                tempStr += c
                lengthNum -= 1
                if lengthNum == 0:
                    output.append(tempStr)
                    tempStr = ""
                    lengthFlag = True
        return output


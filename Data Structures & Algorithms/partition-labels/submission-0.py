class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)
        res = []
        left, right = 0, 0
        active = set()

        while right < len(s):
            counter[s[right]] -= 1

            if counter[s[right]]:
                active.add(s[right])
                right += 1
                continue
            if counter[s[right]] == 0:
                if s[right] in active:
                    active.remove(s[right])
            if not active:
                res.append(right - left + 1)
                left = right + 1
            right += 1
        return res

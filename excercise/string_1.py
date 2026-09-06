class Solution:
    def romanToInt(self, s: str) -> int:
        rom_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        i = len(s) -1
        flag = 1
        while i >= 0:
            # print(s[i])
            if rom_dict[s[i]] < flag:
                sum -= rom_dict[s[i]]
            else:
                sum += rom_dict[s[i]]
            print(sum)
            flag = rom_dict[s[i]]
            i = i-1
        return sum


s = "MCMXCIV"
S = Solution()
print(S.romanToInt(s))


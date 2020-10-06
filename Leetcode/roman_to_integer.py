# https://leetcode.com/problems/roman-to-integer/
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
# Solucion O(n)

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanos = {"I": 1,"V":5,"X":10, "L":50, "C":100, "D": 500, "M": 1000}
        restas5 = {"I":"V", "X":"L","C":"D"}
        restas10 = {"I":"X", "X":"C","C":"M"}
        sumas5 = {"V":"I", "L":"X","D":"C"}
        suma = 0
        x = 0
        while x < len(s):
            roman_value = s[x]
            value = romanos[roman_value]
            if roman_value in ["I","X","C","M"]:
                nextvalue = s[x+1] if len(s) > x+1 else None
                secondnextvalue = s[x+2] if len(s) > x+2 else None
                #Checa si es 2 o 3
                if roman_value == nextvalue:
                    #Es 3?
                    if roman_value == secondnextvalue:
                        multiplo = 3
                        x += 3
                    #Es dos
                    else:
                        multiplo = 2
                        x += 2
                elif nextvalue is not None and nextvalue == restas5.get(roman_value):
                    five = restas5[roman_value]
                    value = romanos[five] - value
                    multiplo = 1
                    x += 2
                #El valor es 9
                elif nextvalue is not None and nextvalue == restas10.get(roman_value):
                    ten = restas10[roman_value]
                    value = romanos[ten] - value
                    multiplo = 1
                    x += 2
                #El valor es 1
                else:
                    multiplo = 1
                    x += 1
            elif roman_value in ["V","L","D"]:
                nextvalue = s[x+1] if len(s) > x+1 else None
                secondnextvalue = s[x+2] if len(s) > x+2 else None
                thirdnextvalue = s[x+3] if len(s) > x+3 else None
                if sumas5[roman_value] == nextvalue:
                    if nextvalue == secondnextvalue:
                        # es 8
                        if nextvalue == thirdnextvalue:
                            multiplo = 1.6
                            x += 4
                        # es 7
                        else:
                            multiplo = 1.4
                            x += 3
                    # es 6
                    else:
                        multiplo = 1.2
                        x += 2
                # es 5
                else:
                    multiplo = 1
                    x += 1

            if suma != 0 and suma < value * multiplo:
                return 0
            suma += int(value * multiplo)
            
        return suma

if __name__ == "__main__":
    s = Solution()
    romanos = ["III","IV","IX","LVIII","MCMXCIV","MMDCCCLXXXVIII","VIIIL","CCCXLV","XLCCCV","M"]
    for romano in romanos:
        print("Integer of {} is {}".format(romano,s.romanToInt(romano)))
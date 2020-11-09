"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t. 
If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.
"""

def minWindowv1(s, t):
    """
    Force brute
    """
    contain_t = {}
    min_window = ""
    for i in t:
        contain_t[i] = contain_t.get(i,0) + 1
    for j in range(0,len(s)):
        #print("Analizando desde {} = {}".format(j,s[j]))
        contain_s = {}
        x = j
        y = j
        string_found = False
        while y < len(s) and not string_found:
            #print("--Revisando hasta {}".format(s[y]))
            contain_s[s[y]] = contain_s.get(s[y],0) + 1
            if contain_t.get(s[y],0) > 0 and contain_s[s[y]] == contain_t.get(s[y],0):
                #print("Existe {} en t".format(s[y]))
                string_found = True
                for a, b in contain_t.items():
                    if contain_s.get(a,0) < b:
                        string_found = False
                        break
            if not string_found:
                y += 1
            #else:
                #print("Se tiene la subcadena {}".format(s[x:y+1]))
        if string_found:
            if len(min_window) > len(s[x:y+1]) or len(min_window) == 0:
                min_window = s[x:y+1]
            #print("Subcadena actual es {}".format(min_window))
    return min_window

def minWindowv2(s, t):
    """
    Window
    """
    contain_t = {}
    min_window = ""
    for i in t:
        contain_t[i] = contain_t.get(i,0) + 1
    x = 0
    minSubstring = ""
    while x < len(s):
        y = x
        contain_s = {}
        found = ""
        while y < len(s):
            #print("{} - {}".format(x,y))
            contain_s[s[y]] = contain_s.get(s[y], 0) + 1
            if not __coversAll(contain_s, contain_t):
                y += 1
            else:
                found = s[x:y+1]
                break
        if found:
            #print("Empieza reducción de {}".format(found))
            while __coversAll(contain_s, contain_t):
                contain_s[s[x]] = contain_s.get(s[x], 0) - 1
                x += 1
            x -= 1
            if len(minSubstring) > len (s[x:y+1]) or minSubstring == "":
                minSubstring = s[x:y+1]
            
        x += 1
        #value = input("x= {}, y= {}, minSubstring = {}. Continuar?:\n".format(x,y,minSubstring))
    return minSubstring

        


def __coversAll(hashContainer, hashObjective):
    for iObjective, vObjective in hashObjective.items():
        valueContainer = hashContainer.get(iObjective,0)
        if valueContainer < vObjective:
            return False
    return True


def printResult(s,t):
    print("*"*100)
    print("Version 1.- Minimum Window Substring searching {} in {} =  {}".format(t,s,minWindowv1(s, t))) 
    print("Version 2.- Minimum Window Substring searching {} in {} =  {}".format(t,s,minWindowv2(s, t))) 


if __name__ == "__main__":
    printResult("ADOBECODEBANC", "ABC")
    printResult("a","a")
    printResult("mmm","a")
    printResult("bdab","ab")
    printResult("cabwefgewcwaefgcf", "cae")
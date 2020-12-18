"""
From 4 list get all the combinations of 4 values in every list which sum equals 0
"""

def fourSum2(l1,l2,l3,l4):
    #Asume than l1[a] + l2[b] = l3[c] + l4[d].
    # Let's find all sums on l1 and l2
    possiblesums = {}
    for a in l1:
        for b in l2:
            sum = a + b
            possiblesums[sum] = possiblesums.get(sum,0) + 1
    result = 0
    #Now, we will check if negative sum are found on previous combinations
    for c in l3:
        for d in l4:
            sum = (c + d)*-1
            result += possiblesums.get(sum,0)
    return result

def printResult(l1,l2,l3,l4):
    print("*"*100)
    print("Combinations between {}, {}, {}, {} which sums zero are {} ".format(l1,l2,l3,l4,fourSum2(l1,l2,l3,l4))) #2


if __name__ == "__main__":
    printResult([1,2],[-2,-1],[-1,2],[0,2])
    printResult([-1,1],[1,-1],[-2,2],[2,-2])
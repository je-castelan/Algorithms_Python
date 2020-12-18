import random 

def max_k_sum_force_brute(arr,k):
    # We can check on samples than complexity timer is O(n*k + k) -> O(n*k). n = arr's length 
    pasos = 0
    maxsum = -99999
    for i in range(len(arr)+1-k):
        tempsum = 0
        for j in range(i,i+k):
            tempsum += arr[j]
            pasos += 1
        maxsum = max(tempsum,maxsum)
    return maxsum,pasos


def max_k_sum_slicing_window(arr,k):
    #The window consist to point to the required elements to compare, removing old elements and
    #adding new elements, avoiding force brute.
    #Complexity time is O(n-k) -> O(n)
    pasos = 0
    tmpsum = sum([arr[i] for i in range(0,k)])
    maxsum = tmpsum
    for j in range(k,len(arr)):
        tmpsum = tmpsum + arr[j] - arr[j-k]
        maxsum = max(tmpsum,maxsum)
        pasos += 1
    return maxsum, pasos

def printResult(arr,k,printlist = True):
    print("*"*100)
    suma, pasos = max_k_sum_force_brute(arr,k)
    print("Max sum with {} elements on {} with force brute is {} in {} steps".format(k,arr if printlist else "[lista]",suma,pasos))
    suma, pasos = max_k_sum_slicing_window(arr,k)
    print("Max sum with {} elements on {} with slicing window is {} in {} steps".format(k,arr if printlist else "[lista]",suma,pasos))

if __name__ == "__main__":
    printResult([80,-50,90,100],2)
    printResult([80,-50,90,100,-30,200,-10,210],2)
    printResult([40,30,90,-20,70,-50,100],2)
    printResult([40,30,90,-20,70,-50,100,200],3)
    printResult([1, 2, 100, -1, 5],3)

    largelist = random.sample(range(0, 10000), 10000)

    printResult(largelist, 3, printlist=False)
    printResult(largelist, 4, printlist=False)
    printResult(largelist, 15, printlist=False)

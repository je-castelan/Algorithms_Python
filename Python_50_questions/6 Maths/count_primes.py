
def primes(number):
    """
    Count the number of prime numbers less than a non-negative number, n.
    It must apply the sieve of eratosthenes
    """
    array = [False] * 2 + [True]*(number - 2)
    i = 2
    while (i ** 2) <= number - 1: #We need only check the numbers before the argument
        #print("Analicemos número y primos de {}".format(i))
        if array[i]:
            n = 2
            #print("Ups!!! {} ya es primo".format(i))
            while (i * n) <= number - 1:
                #print("{} * {} = {} es primo".format(i,n, i*n))
                array[i * n] = False
                n += 1
        i += 1
    return sum(array)


def printResult(number):
    print("*"*100)
    print("Primes before {} on my version are {}".format(number,primes(number)))


if __name__ == "__main__":
    printResult(10)
    printResult(45)
    printResult(34)
    printResult(0)
    printResult(1)
    printResult(2)
    printResult(3)
    #printResult(100)
    #printResult(1000)
    #printResult(10000)
    
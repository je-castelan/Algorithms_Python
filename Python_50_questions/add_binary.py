
def add_binary(a,b):
    b = (("0"*(len(a)-len(b))) + b) if len(a) > len(b) else b
    a = (("0"*(len(b)-len(a))) + a) if len(b) > len(a) else a
    sum = ""
    acum = 0
    for i in range(len(a) - 1, -1, -1):
        vala = int(a[i])
        valb = int(b[i])
        suma = acum + vala + valb
        sum = ("0" if (suma == 0 or suma == 2) else "1") + sum
        acum = 1 if suma >= 2 else 0
    if acum:
        sum = "{}{}".format(acum,sum)
    return sum



def printResult(a,b):
    print("*"*100)
    print("Binary {} + {} = {}".format(a,b,add_binary(a,b)))


if __name__ == "__main__":
    printResult("11","1") #100
    printResult("1010","1011") #10101
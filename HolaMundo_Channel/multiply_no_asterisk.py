def multiply_no_asterisk(a,b):
    # Returns a * b with no using *
    # Challenge of Hola Mundo Channel on https://www.youtube.com/watch?v=MXmQM_Uehtk&t=584s
    result = 0
    sign = 1 if ((a >= 0 and b >= 0) or (a < 0 and b < 0)) else -1
    for i in range(abs(b)):
        result += abs(a)
    return result * sign

if __name__ == "__main__":
    testings = [[3,4],[0,0],[-5,9],[-15,-4],[49,-35],[99,99],[-99,-99],[1,1]]
    for testing in testings:
        print("{} por {} es {}".format(testing[0],testing[1],multiply_no_asterisk(testing[0],testing[1])))
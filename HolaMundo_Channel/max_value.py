import functools

def maxvalue(arr):
    # Get greater value on array in one iteration
    # Challenge of Hola Mundo Channel on https://www.youtube.com/watch?v=MXmQM_Uehtk&t=584s

    #Comment lines are my first version. I supplied it with a reduce function than I learned on https://www.python-course.eu/lambda.php
    #max = 0
    #for value in arr:
    #    max = value if value > max else max
    #return max

    return functools.reduce(lambda x,y: x if x > y else y, arr)

if __name__ == "__main__":
    print(maxvalue([6,34,76,444,2,87,12]))
    print(maxvalue([6,789,76,444,2,87,12]))
    print(maxvalue([50,-1500,1000,0,1,53]))

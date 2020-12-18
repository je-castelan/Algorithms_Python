Python programming challenge
===============================

These exercise are a evidence of my knowledge on Python programming and algorithm design

Challenge are found on the following media

 - [Leetcode](https://leetcode.com/)
 - [Hola Mundo Youtube Channel](https://www.youtube.com/channel/UC4FHiPgS1KXkUMx3dxBUtPg)
 - [LeetCode In Python: 50 Algorithms Coding Interview Questions](https://www.udemy.com/course/leetcode-in-python-50-algorithms-coding-interview-questions/)


# Some important notes
 - Prior of algoritm selection than I learned istrying to check the following order:
    - Mathematic solution (if exist or know)
    - Sort and/or search well-known algoritms
    - Window method: in order to avoid a second checking which could increase the complexity
    - Check list with pointers which checks from the begining and end (try not to modify array)
    - Use hashmap (it will increase complex space but reduce complex time)
    - As last resource, iterate
      - If you don't know how many times iterate, try to use recursive (and also temporaly pointers and variables on the same object in order to not lose control)

There are new kind of data structure than I know in those couses like
- Stack
- Queue
- Graphs


# New learned resources

## Functools

It's a library with functions related to simply operations with arrays. You need to import it manually.

> import functools

These functions works with a lambda function or function in order to take the logical to apply

## Reduce

The syntax is `functools.reduce(function, array)`

With this, you will get a unique value on the array based of the function. The function must need the acumulator variable and the new value in order to adjust the acumulate to new new value

> functools.reduce(lambda x,y: x + y, arr) # It will take the values of `array` and sum them. Fianlly, you will have the sum of all the values

## Filter

Based on a function which return True or False, you will get a list with allowed values

It's important to insert this function into a list initilizacion

> unpairs = list(filter(lambda x: x % 2 ,arr)) # It will return the unpairs numbers on arr list.

## Map

Based on a function, convert the values on a array to the result of the function.

It's important to insert this function into a list initilizacion

> unpairs = list(map(lambda x: x*3 ,arr)) # It will return the values of arr multiplied by 3


## Defaultdict

It's like dictionary object. In this case, when we try to call an unexisting object, it will send a "not present" value insteand to send exception.

We need to import collections

> import collections 

On graphs, we use it with a dict with list values like this

> a = collections.defaultdict(list)

## Infinite float

Instead to declare a variable with a big value, we can use the following function.

> a = float('inf')

## Heapq

This object can work with lists and dicts, automatizing some functions.

We need to import heapq

> import heapq

There are some important funcions

- `heappush`: Insert an element

```
h = []
heapq.heappush(h, value)
```

- `heappop`: Return the lower value and pop it out of the object.

```
h = [5,3,7,4]
a = heapq.heappop(h) # a equals 3
```


# https://leetcode.com/problems/reverse-integer/
# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321
# Solucion O(n)

def reverse_number(number):
    
    sign = 1 if number >= 0 else -1
    number = abs(number)
    position = len(str(number))
    new_number = 0
    
    while position > 0:
        next_number = number % 10
        number = number // 10
        new_number += (next_number * (10**(position-1)))
        position -= 1
    return new_number * sign

if __name__ == "__main__":
    print(reverse_number(123))   
    print(reverse_number(-123))
    print(reverse_number(321))   
    print(reverse_number(-321))
    print(reverse_number(46921))   
    print(reverse_number(-56472))
    print(reverse_number(0))
    print(reverse_number(1000))
    print(reverse_number(59000))
    print(reverse_number(-2143847412))
    print(reverse_number(1534236469))
    
    
    
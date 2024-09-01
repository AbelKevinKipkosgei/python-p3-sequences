#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = []
    a,b = 0,1

    while len(fibonacci_list) < length:
        fibonacci_list.append(a)
        a,b = b, a + b
    print(fibonacci_list)

print_fibonacci(10)
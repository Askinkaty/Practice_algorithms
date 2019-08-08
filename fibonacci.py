#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def fibonacci1(n):
    assert(n>=0)
    a = 0
    b = 1
    print(a)
    if n > 0:
        print(b)
    i = 2
    while i <= n:
        c = a + b
        print(c)
        a = b
        b = c
        i += 1

def fibonacci(n):
    memory = {0: 0, 1: 1}
    def loop(n):
        assert(n>=0)
        if n in memory:
            return memory[n]
        else:
            memory[n] = loop(n-1) + loop(n-2)
            return memory[n]
    return loop(n)
    
            

print(fibonacci(0))
print('---')
print(fibonacci(1))
print('---')
print(fibonacci(10))


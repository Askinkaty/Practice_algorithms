#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest

class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        
        stack.push(5)
        stack.push(4)
        stack.push(3)        
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 5)
        self.assertIsNone(stack.pop())

    def test_balanced_brackets(self):
        self.assertTrue(check_balance('()'))
        self.assertFalse(check_balance(')('))
        self.assertFalse(check_balance('())'))
        self.assertTrue(check_balance('((()))'))
        self.assertFalse(check_balance(')()'))
        self.assertFalse(check_balance('(())))'))

    def test_get_min(self):
        stack = Stack()
        stack.push(5)
        stack.push(4)
        stack.push(3)
        stack.push(8)
        stack.push(3)
        stack.push(1)
        stack.push(10)
        self.assertEqual(stack.get_min(), 1)
        stack.pop()
        self.assertEqual(stack.get_min(), 1)
        stack.pop()
        self.assertEqual(stack.get_min(), 3)
        stack.pop()
        self.assertEqual(stack.get_min(), 3)
        stack.pop()
        self.assertEqual(stack.get_min(), 3)
        stack.pop()
        self.assertEqual(stack.get_min(), 4)
        stack.pop()
        self.assertEqual(stack.get_min(), 5)
        stack.pop()
        self.assertIsNone(stack.get_min())

        
class Stack:
    def __init__(self):
        self.top = None
        self.history = None
        
    def push(self, value):
        new_element = Stack._StackElement(value)
        new_element.next = self.top
        self.top = new_element
        if self.history is None or value <= self.history.value:
            new_history_element = Stack._StackElement(value)
            new_history_element.next = self.history
            self.history = new_history_element
        
    def pop(self):
        if self.top is not None:            
            result = self.top.value
            self.top = self.top.next
            if result == self.history.value:
                self.history = self.history.next
            return result
        else:
            return None

    def is_empty(self):
        return self.top is None


    def get_min(self):
        return self.history.value if self.history is not None else None
            
        
        
        
    class _StackElement:
        def __init__(self, value):
            self.value = value
            self.next = None

            
def check_balance(s):
    stack = Stack()
    for c in s:
        if c == '(':
            stack.push(c)
        else:
            popped = stack.pop()
            if popped is None:
                return False
    if stack.is_empty():
        return True
    else:
        return False


    

if __name__ == '__main__':
    unittest.main()

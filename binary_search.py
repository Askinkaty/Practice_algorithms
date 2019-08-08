#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest


class TestSearch(unittest.TestCase):
    def test_empty(self):
        result = binary_search([], 5)
        self.assertIsNone(result)
        
    def test_all_equal(self):
        result = binary_search([5, 5, 5, 5, 5], 5)
        self.assertIsNotNone(result)

    def test_regular(self):
        result = binary_search([1, 3, 5, 7, 8, 10, 12, 23, 42], 5)
        self.assertEqual(result, 2)

    def test_regular_42(self):
        result = binary_search([1, 3, 5, 7, 8, 10, 12, 23, 42], 42)
        self.assertEqual(result, 8)

    def test_regular_not_found(self):
        result = binary_search([1, 3, 5, 7, 8, 10, 12, 23, 42], 9)
        self.assertIsNone(result)
        


def binary_search1(l, n):
    start = 0
    end = len(l)
    while start < end:
        mid = (start + end) // 2
        if n < l[mid]:
            end = mid - 1
        elif n == l[mid]:
            return mid
        else:
            start = mid + 1
        
def binary_search(l, n):
    def find(start, end):
        if start < end:
            mid = (start + end) // 2
            if n < l[mid]:
                return find(start, mid)
            elif n == l[mid]:
                return mid
            else:
                return find(mid + 1, end)
            
    return find(0, len(l))
    

        
if __name__ == '__main__':
    unittest.main()

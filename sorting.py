#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import unittest

class TestSort(unittest.TestCase):
    def setUp(self):
        self.empty = []
        self.one_el = [1]
        self.all_sorted = [1, 3, 7, 15, 23, 41, 99]
        self.reverted = [99, 41, 23, 15, 7, 3, 1]
        self.regular = [3, 99, 1, 23, 7, 41, 15]
        self.the_same = [5, 5, 5, 5, 5]
        self.all_cases = [self.empty, self.one_el, self.the_same, self.all_sorted,
                          self.reverted, self.regular]
        #self.all_cases = [self.regular]
        
    def test_bubble(self):
        for test_data in self.all_cases:
            expected = sorted(test_data)
            bubble_sort(test_data)
            self.assertEqual(test_data, expected)
    def test_merge(self):
        for test_data in self.all_cases:
            expected = sorted(test_data)
            merge_sort(test_data)
            self.assertEqual(test_data, expected)

    def test_insertion(self):
        for test_data in self.all_cases:
            expected = sorted(test_data)
            insertion_sort(test_data)
            self.assertEqual(test_data, expected)

    def test_quick(self):
        for test_data in self.all_cases:
            expected = sorted(test_data)
            quick_sort(test_data)
            self.assertEqual(test_data, expected)



            
def bubble_sort(l):
    for _ in range(len(l)):
        swap_happened = False
        for j in range(len(l) - 1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                swap_happened = True
        if not swap_happened:
            break


def merge_sort(l):
    def inner(start, end):
        total_len = end - start
        #print(start, end, total_len)
        if total_len <= 1:
            return
        elif total_len == 2:
            if l[start] > l[end - 1]:
                l[start], l[end - 1] = l[end - 1], l[start]
        elif total_len > 2:
            mid = start + total_len // 2
            inner(start, mid)
            inner(mid, end)
            merge(start, mid, end)
    def merge(start, mid, end):
        output = []
        left_i = start
        right_i = mid
        while left_i < mid and right_i < end:
            if l[left_i] <= l[right_i]:
                output.append(l[left_i])
                left_i += 1
            else:
                output.append(l[right_i]) 
                right_i += 1
        while left_i < mid:
            output.append(l[left_i])
            left_i += 1
        while right_i < end:
            output.append(l[right_i])
            right_i += 1
        l[start:end] = output
    inner(0, len(l))


def insertion_sort(l):
    for current in range(1, len(l)):
        for j in range(current, 0, -1):
            if l[j] < l[j-1]:            
                l[j], l[j-1] = l[j-1], l[j]
        

def quick_sort(l):
    def sort(start, end):
        if start < end:
            p = partition(start, end)
            sort(start, p)
            sort(p + 1, end)

    def partition(start, end):
        pivot = end - 1
        i = start - 1
        for j in range(start, pivot):
            if l[j] < l[pivot]:
                i += 1
                l[j], l[i] = l[i], l[j]
        assert i < pivot
        if l[pivot] < l[i + 1]:
            l[i + 1], l[pivot] = l[pivot], l[i + 1]
        return i + 1
    sort(0, len(l))
    
        
if __name__ == '__main__':
    unittest.main()

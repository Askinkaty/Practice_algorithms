#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import unittest

class BinaryTreeTest(unittest.TestCase):
    def setUp(self):
        node_23 = Node(23)
        node_17 = Node(17)
        node_99 = Node(99)
        node_50 = Node(50)
        node_3 = Node(3)
        node_10 = Node(10)

        node_23.left = node_17
        node_23.right = node_3
        node_17.left = node_99
        node_17.right = node_50
        node_3.left = node_10
        self.root = node_23

    def test_dfs(self):
        result = self.root.dfs()
        expected = [99, 17, 50, 23, 10, 3]
        self.assertEqual(result, expected)

    def test_bfs(self):
        result = self.root.bfs()
        expected = [23, 17, 3, 99, 50, 10]
        self.assertEqual(result, expected)
        
    def test_map(self):
        fun = lambda x: x * 2
        result = self.root.map(fun).dfs()
        expected = [198, 34, 100, 46, 20, 6]
        self.assertEqual(result, expected)

    def test_aggregate(self):
        fun = lambda x, y: x + y
        result = self.root.aggregate(0, fun)
        expected = sum(self.root.dfs())
        self.assertEqual(result, expected)

    def test_revert(self):
        result = self.root.revert().dfs()
        expected = [3, 10, 23, 50, 17, 99]
        self.assertEqual(result, expected)

    def test_find_max_min_depth(self):
        node_17 = Node(17)
        self.root.right.left.right = node_17
        expected_min = 2
        expected_max = 3
        minim, maxim = self.root.find_max_min_depth()
        self.assertEqual(minim, expected_min)
        self.assertEqual(maxim, expected_max)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def dfs(self):
        result = []
        if self.left is not None:
            result.extend(self.left.dfs())
        result.append(self.value)
        if self.right is not None:
            result.extend(self.right.dfs())
        return result

    def bfs(self):
        result = []
        result.append(self.value)
        result.extend(self._selfless_bfs())        
        return result

    def _selfless_bfs(self):
        result = []
        children = [self.left, self.right]
        children = [x for x in children if x is not None]
        for child in children:
            result.append(child.value)
        for child in children:
            result.extend(child._selfless_bfs())
        return result

    def revert(self):
        new_root = Node(self.value)
        if self.left is not None:
            new_root.right = self.left.revert()
        if self.right is not None:
            new_root.left = self.right.revert()
        return new_root
            
    def map(self, function):
        new_root = Node(function(self.value))
        if self.left is not None:
            new_root.left = self.left.map(function)
        if self.right is not None:
            new_root.right = self.right.map(function)
        return new_root

    def aggregate(self, initial, function):
        agg = function(initial, self.value)
        if self.left is not None:
            agg = self.left.aggregate(agg, function)
        if self.right is not None:
            agg = self.right.aggregate(agg, function)
        return agg

    
    def find_max_min_depth(self):
        if self.left is None and self.right is None:
            return 0, 0      
        minim = None
        maxim = None
        if self.left is not None:
            minim, maxim = self.left.find_max_min_depth()
            minim += 1
            maxim += 1
        if self.right is not None:
            right_min, right_max = self.right.find_max_min_depth()
            right_min += 1
            right_max += 1
            if minim is None or minim > right_min:
                minim = right_min
            if maxim is None or maxim < right_max:
                maxim = right_max
        
        return minim, maxim
        
            
if __name__ == '__main__':
    unittest.main()

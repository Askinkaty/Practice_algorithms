#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import math
import unittest

class GraphTest(unittest.TestCase):
    def setUp(self):
        self.graph = [
            [0, 1, 0, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 1, 0, 0],
            [1, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 0]
        ]
        self.w_graph =  [
            [0, 5, 0, 0, 1, 0, 0, 0],
            [5, 0, 2, 0, 30, 0, 0, 0],
            [0, 2, 0, 3, 0, 0, 0, 0],
            [0, 0, 3, 0, 40, 1, 0, 0],
            [1, 30, 0, 40, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 2, 0]
        ]
    def test_connectivity_general(self):
        result = check_connected(self.graph)
        self.assertFalse(result)
    def test_connectivity_simple_connected(self):
        graph = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
        result = check_connected(graph)
        self.assertTrue(result)
    def test_min_distances(self):
        result = min_distances(self.graph, 4)
        self.assertEqual(result, [1, 1, 2, 1, 0, 2, None, None])
    def test_min_w_distances(self):
        result = min_distances(self.w_graph, 4)
        self.assertEqual(result, [1, 6, 8, 11, 0, 12, None, None])


def check_connected_rec(graph):
    all_nodes = len(graph)
    #print(all_nodes)
    visited_nodes = set()

    def loop(node):
        #print('Node {0}'.format(node))
        #print(visited_nodes)
        if node not in visited_nodes:
            visited_nodes.add(node)
            neighbours = [i for i, el in enumerate(graph[node]) if el==1]
            #print(neighbours)
            for neighbour in neighbours:
                loop(neighbour)
                
    loop(0)
    return len(visited_nodes) == all_nodes
    

def check_connected(graph):
    visited_nodes = set()
    front = set()
    front.add(0)
    while len(front) > 0:
        #print(front)
        node = front.pop()
        if node not in visited_nodes:
            visited_nodes.add(node)
            neighbours = [i for i, el in enumerate(graph[node]) if el==1]
            for n in neighbours:
                front.add(n)  
                
    return len(visited_nodes) == len(graph)


def min_distances(graph, origin):
    result = [None] * len(graph)
    visited_nodes = set()
    front = set()
    result[origin] = 0
    front.add(origin)
    while len(front) > 0:
        node = front.pop()
        node_distance = result[node]
        if node not in visited_nodes:
            neighbours = [i for i, el in enumerate(graph[node]) if el!=0]
            neighbours.sort(key=lambda x: graph[node][x])
            for n in neighbours:
                if n not in visited_nodes:
                    n_distance = result[n]
                    edge_weight = graph[node][n]
                    if n_distance is None or n_distance > node_distance + edge_weight:
                        result[n] = node_distance + edge_weight
                    front.add(n)
            visited_nodes.add(node)
    return result
    


    



if __name__== '__main__':
    unittest.main()

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import unittest
from stack import Stack

class LinkedListTest(unittest.TestCase):
    def test_construct_from_source(self):
        expected = "< 12 99 37 88 0 >"
        linked_list = LinkedList([12, 99, 37, 88, 0])
        self.assertEqual(str(linked_list), expected)

    def test_construct_from_empty_source(self):
        linked_list = LinkedList(None)
        self.assertEqual(linked_list.get_head(), None)

    def test_find_not_empty_exists(self):
        linked_list = LinkedList()
        linked_list.prepend(99)
        linked_list.prepend(37)
        linked_list.prepend(99)
        linked_list.prepend(12)
        result = linked_list.find(99)
        self.assertEqual(result.get_value(), 99)
        self.assertIsNotNone(result.get_next())
        self.assertEqual(result.get_next().get_value(), 37)

    def test_find_not_empty_not_exists(self):
        linked_list = LinkedList()
        linked_list.prepend(37)
        linked_list.prepend(99)
        linked_list.prepend(12)
        self.assertIsNone(linked_list.find(100))

    def test_find_empty(self):
        linked_list = LinkedList()
        self.assertIsNone(linked_list.find(13))

    def test_delete_empty(self):
        linked_list = LinkedList()
        linked_list.delete(42)
        self.assertEqual(linked_list.get_head(), None)

    def test_delete_head(self):
        linked_list = LinkedList([12, 99, 37])
        linked_list.delete(12)
        expected = '< 99 37 >'
        self.assertEqual(str(linked_list), expected)

    def test_delete_not_head(self):
        linked_list = LinkedList([12, 99, 37])
        linked_list.delete(99)
        expected = '< 12 37 >'
        self.assertEqual(str(linked_list), expected)

    def test_iterator(self):
        linked_list = LinkedList([12, 99, 37])
        python_list = list(linked_list)
        #print(python_list))
        #for el in linked_list:
        #    print(el)
        self.assertEqual(len(python_list), 3)
        self.assertEqual(python_list[0], 12)
        self.assertEqual(python_list[1], 99)
        self.assertEqual(python_list[2], 37)

    def test_insert(self):
        linked_list = LinkedList([12, 99, 37])
        linked_list.insert(66, 12)
        expected = '< 12 66 99 37 >'
        self.assertEqual(str(linked_list), expected)

    def test_copy(self):
        linked_list = LinkedList([12, 99, 37])
        expected = '< 12 99 37 >'
        result = linked_list.copy()
        self.assertEqual(str(result), expected)

    def test_copy_empty(self):
        linked_list = LinkedList()
        expected = '< >'
        result = linked_list.copy()
        self.assertEqual(str(result), expected)     

    def test_map(self):
        fun = lambda x: x * 2
        linked_list = LinkedList([2, 9, 3])
        expected = '< 4 18 6 >'
        result = linked_list.map(fun)
        self.assertEqual(str(result), expected)

    def test_aggregate(self):
        fun = lambda x, y: x + y
        linked_list = LinkedList([2, 9, 3])
        result = linked_list.aggregate(0, fun)
        expected = 14
        self.assertEqual(result, expected)

    def test_get_n(self):
        linked_list = LinkedList([2, 9, 3, 8, 10])
        result = linked_list.get_n(3)
        self.assertEqual(result, 8)
        
    def test_get_k_from_end(self):
        linked_list = LinkedList([2, 9, 3, 8, 10])
        result = linked_list.get_k_from_end(3)
        self.assertEqual(result, 9)

    def test_get_k_from_end_last(self):
        linked_list = LinkedList([2, 9, 3, 8, 10])
        result = linked_list.get_k_from_end(4)
        self.assertEqual(result, 2)
   
    def test_get_k_from_end_not_present(self):
        linked_list = LinkedList([2, 9, 3, 8, 10])
        result = linked_list.get_k_from_end(5)
        self.assertEqual(result, None)

    def test_reverted(self):
        linked_list = LinkedList([2, 9, 3, 8, 10])
        result = linked_list.revert()
        expected = '< 10 8 3 9 2 >'
        self.assertEqual(str(result), expected)

    def test_filter(self):
        linked_list = LinkedList([2, 9, 3, 8, 10])
        fun = lambda x: x > 5
        result = linked_list.filter(fun)
        expected = '< 9 8 10 >'
        self.assertEqual(str(result), expected)

    def test_sum_two_lists(self):
        linked_list_1 = LinkedList([3, 9, 7, 9])
        linked_list_2 = LinkedList([8, 1, 4])
        result = linked_list_1.plus(linked_list_2)
        expected = '< 1 1 2 0 1 >'
        self.assertEqual(str(result), expected)
        
    def test_plus_direct(self):
        linked_list_1 = LinkedList([9, 7, 9, 3])
        linked_list_2 = LinkedList([4, 1, 8])
        result = linked_list_1.plus_direct(linked_list_2)
        expected = '< 1 0 2 1 1 >'
        self.assertEqual(str(result), expected)
        
        
        
class LinkedList:
    class _Iterator:
        def __init__(self, head):
            self._current = head
        def __next__(self):
            if self._current is not None:
                result = self._current.get_value()
                self._current = self._current.get_next()
                return result
            else:
                raise StopIteration()
            
    def __init__(self, source=None):
        if source:
            it = iter(source)
            self._head = ListElement(next(it))
            previous = self._head
            for el in it:
                current = ListElement(el)
                previous.set_next(current)
                previous = current
        else:
            self._head = None

    def __str__(self):
        s = ''
        current = self._head
        while current != None:
            s = s + ' ' + str(current.get_value())
            current = current.get_next()
        s = '<' + s + ' >'
        return s

            
    def __iter__(self):
        #return LinkedList._Iterator(self._head)
        current = self._head
        while current is not None:
            yield current.get_value()
            current = current.get_next()

    def get_head(self):
        return self._head
    
            
    def prepend(self, value):
        current = ListElement(value)
        current.set_next(self._head)
        self._head = current

    def get_n(self, n):
        c = 0
        current = self._head
        while current is not None:
            if c == n:
                return current.get_value()
            else:
                c += 1
                current = current.get_next()
        return None

    def get_k_from_end(self, k):
        current = self._head
        flag = current
        for i in range(k+1):
            if flag is not None:
                flag = flag.get_next()
            else:
                return None
        while flag is not None:
            current = current.get_next()
            flag = flag.get_next()
        return current.get_value()

    def revert_old(self):
        reverted = LinkedList()
        current = self._head
        while current is not None:
            new_element = ListElement(current.get_value())
            new_element.set_next(reverted._head)
            reverted._head = new_element
            current = current.get_next()
        return reverted

    def revert(self):
        reverted = LinkedList()
        def loop(current):
            if current is not None:
                new_element = ListElement(current.get_value())
                new_element.set_next(reverted._head)
                reverted._head = new_element
                loop(current.get_next())
        loop(self._head)
        return reverted

    def filter(self, predicate):
        new_list = LinkedList()
        def loop(current):
            if current is not None:
                if predicate(current.get_value()):
                    new_element = ListElement(current.get_value())
                    new_element.set_next(loop(current.get_next()))
                    return new_element
                else:
                    return loop(current.get_next())
            else:
                return None

        new_list._head = loop(self._head)
        return new_list
    
    def find(self, value):
        previous, current = self._find(value)
        return current

    def _find(self, value):
        current = self._head
        previous = None
        while current != None:
            if current.get_value() == value:
                return previous, current
            previous = current
            current = current.get_next()
        return None, None

    def delete(self, value):
        previous, current = self._find(value)
        if current is None:
            return
        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())
        current.set_next(None)

    def insert(self, value, previous_value):
        _, previous = self._find(previous_value)
        if previous is None:
            return
        else:
            new_element = ListElement(value)
            following = previous.get_next()
            previous.set_next(new_element)
            new_element.set_next(following)

    def copy_old(self):
        copy = LinkedList()
        if self._head is not None:
            it = iter(self)
            copy._head = ListElement(next(it))
            current = copy._head
            for el in it:
                new_element = ListElement(el)
                current.set_next(new_element)
                current = new_element
        return copy

    def copy(self):
        return self.map(lambda x: x)

    def map(self, function):
        mapped = LinkedList()
        if self._head is not None:
            it = iter(self)
            mapped._head = ListElement(function(next(it)))
            current = mapped._head
            for el in it:
                new_element = ListElement(function(el))
                current.set_next(new_element)
                current = new_element
        return mapped
    
    def aggregate(self, initial, function):
        agg = initial
        for el in self:
            agg = function(agg, el)
        return agg

    def plus(self, other):
        new_list = LinkedList()
        current = None
        a = self._head
        b = other._head
        carry = 0
        while a is not None or b is not None:
            summ = carry
            if a is not None:
                summ += a.get_value()
                a = a.get_next()
            if b is not None:
                summ += b.get_value()
                b = b.get_next()
            carry = summ // 10
            new_value = summ % 10
            
            new_element = ListElement(new_value)
            if new_list._head is None:
                new_list._head = new_element
                current = new_list._head
            else:
                current.set_next(new_element)
                current = new_element
        if carry != 0:
            new_element = ListElement(carry)
            current.set_next(new_element)
        return new_list


    def plus_direct(self, other):
        stack1 = Stack()
        stack2 = Stack()
        for el in self:
            stack1.push(el)
        for el in other:
            stack2.push(el)
        new_list = LinkedList()
        current = None
        a = stack1.pop()
        b = stack2.pop()
        carry = 0
        while a is not None or b is not None:
            summ = carry
            if a is not None:
                summ += a
                a = stack1.pop()
            if b is not None:
                summ += b
                b = stack2.pop()
            carry = summ // 10
            new_value = summ % 10
            new_list.prepend(new_value)
        if carry != 0:
            new_list.prepend(carry)
        return new_list
        
        
        
class ListElement:
    def __init__(self, value):
        self._value = value
        self._next = None
        
    def get_value(self):
        return self._value

    def get_next(self):
        return self._next

    def set_next(self, new_next):
        self._next = new_next



if __name__ == '__main__':
    unittest.main()

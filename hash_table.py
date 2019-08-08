#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest


class HashTableTest(unittest.TestCase):
    def test_insert_get_value(self):
        hash_table = HashTable()
        hash_table['first'] = 10
        self.assertEqual(hash_table['first'], 10)
        hash_table['first'] = 3
        self.assertEqual(hash_table['first'], 3)
        hash_table['second'] = 5
        self.assertEqual(hash_table['first'], 3)
        self.assertEqual(hash_table['second'], 5)
        del hash_table['first']
        with self.assertRaises(KeyError):
            hash_table['first']

    def test_resize(self):
        hash_table = HashTable()
        for i in range(100000):
            #if i % 100 == 0:
            #    print(i)
            hash_table[i] = i
        for i in range(100000):
            self.assertEqual(hash_table[i], i)
    def test_iteration(self):
        hash_table = HashTable()
        for i in range(100):
            hash_table[i] = str(i)
        target_keys = set(range(100))
        for key in hash_table:
            #print(type(key))
            #print(target_keys)
            #print(key in target_keys)
            self.assertTrue(key in target_keys)
            target_keys.remove(key)
        self.assertEqual(len(target_keys), 0)


class HashTable():
    def __init__(self):
        self._bucket_count = 16
        self._buckets = HashTable._create_buckets(self._bucket_count)
        self._key_count = 0


    class _Iterator():
        def __init__(self, buckets):
            self._buckets = buckets
            self._current_bucket = 0
            self._current_index = -1
        def __next__(self):
            if len(self._buckets) <= 0:
                raise StopIteration()

            self._current_index += 1            
            if self._current_index >= len(self._buckets[self._current_bucket]):
                self._current_bucket += 1
                self._current_index = 0
            if self._current_bucket >= len(self._buckets):
                raise StopIteration()
            result = self._buckets[self._current_bucket][self._current_index][0]
            return result
            
    def __iter_old__(self):
        return HashTable._Iterator(self._buckets)

    def __iter__(self):
        for bucket in self._buckets:
            for el in bucket:
                yield el[0]
        
        
    @staticmethod
    def _create_buckets(count):
        buckets = []
        for i in range(count):
            buckets.append([])
        return buckets

    def _get_bucket_idx(self, key):
        return hash(key) % self._bucket_count   
        

    def __setitem__(self, key, value):
        self._resize_if_needed()
        bucket_idx = self._get_bucket_idx(key)
        for i, el in enumerate(self._buckets[bucket_idx]):
            if el[0] == key:
                self._buckets[bucket_idx][i] = (key, value)
                return
        self._buckets[bucket_idx].append((key, value))
        self._key_count += 1

    def __getitem__(self, key):
        bucket_idx = self._get_bucket_idx(key)
        for el in self._buckets[bucket_idx]:
            if el[0] == key:
                return el[1]
        raise KeyError(key)

    def __delitem__(self, key):
        bucket_idx = self._get_bucket_idx(key)
        for i, el in enumerate(self._buckets[bucket_idx]):
            if el[0] == key:
                del self._buckets[bucket_idx][i]
                self._key_count -= 1
                return
        raise KeyError(key)

    def _resize_if_needed(self):
        if self._key_count / self._bucket_count >= 10:
            new_bucket_count = self._bucket_count * 2
            new_buckets = HashTable._create_buckets(new_bucket_count)
            for bucket in self._buckets:
                for el in bucket:
                    new_hash = hash(el[0]) % new_bucket_count
                    new_buckets[new_hash].append(el)
            self._buckets = new_buckets
            self._bucket_count = new_bucket_count


if __name__ == '__main__':
    unittest.main()

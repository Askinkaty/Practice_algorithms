#!/usr/bin/env python3
# -*- conding:utf-8 -*-

def permutations(s):
    variants = set(range(len(s)))

    def loop(variants):
        if len(variants) == 0:
            return ['']
        result = []
        for v in variants:
            next_variants = set(variants)
            next_variants.remove(v)
            for next_perms in loop(next_variants):
                result.append(s[v] + next_perms)
        return result
    return loop(variants)

print(permutations('abc'))

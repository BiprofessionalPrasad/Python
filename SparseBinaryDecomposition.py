# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 14:11:42 2025

@author: prasa
"""

def is_sparse(n: int) -> bool:
    return (n & (n >> 1)) == 0

def solution(N: int) -> int:

    if is_sparse(N):
        return N
    P = 0
    for i in range(29, -1, -1):
        n_bit_is_set = (N >> i) & 1
        if n_bit_is_set:
            p_next_bit_is_set = (i < 29) and ((P >> (i + 1)) & 1)
            if not p_next_bit_is_set:
                P |= (1 << i)
    return P

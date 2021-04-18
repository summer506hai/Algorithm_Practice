# -*- coding: utf-8 -*-
#pytest
import candy_swap

def test_fairCandySwap():
    x1 = [1, 2, 5]
    y1 = [2, 4]
    val1 = candy_swap.fairCandySwap(x1,y1)
    assert val1 == [5,4]
    val1_dic = candy_swap.fairCandySwap_use_dic(x1,y1)
    assert val1_dic == [5, 4]